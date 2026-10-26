// Validate the same embedded content, formula engine and link mapping used offline.
const fs=require('node:fs');
const path=require('node:path');
const root=path.resolve(__dirname,'..');
const katex=require(path.join(root,'assets/vendor/katex.js'));
const marked=require(path.join(root,'assets/vendor/marked.js'));
const files=fs.readdirSync(root).filter(n=>n.endsWith('.html')).map(n=>path.join(root,n));
for(const ch of ['chapter4','chapter5'])for(const name of fs.readdirSync(path.join(root,ch)))if(name.endsWith('.html'))files.push(path.join(root,ch,name));
let formulas=0,links=0;
for(const file of files){
 const source=fs.readFileSync(file,'utf8');
 const data=JSON.parse(source.match(/<script type="application\/json" id="data">([\s\S]*?)<\/script>/)[1]);
 const tokenized=data.markdown.replace(/\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$/g,(whole,block,inline)=>{
   try{katex.renderToString(block??inline,{displayMode:block!==undefined,throwOnError:true,strict:'ignore'});}catch(e){throw new Error(path.relative(root,file)+': '+e.message);}
   formulas++;return 'MATH';
 });
 const rendered=marked.parse(tokenized);
 for(const [_,attr,original] of (source+rendered).matchAll(/\b(href|src)="([^"<>]+)"/g)){
  const target=data.links[original]??data.links[decodeURI(original)]??original;
  if(/^(?:https?:|#|mailto:)/.test(target))continue;
  if(target.includes('.md'))throw new Error('Unmapped Markdown link in '+file+': '+target);
  const local=decodeURIComponent(target.split(/[?#]/)[0]);
  const dest=path.resolve(path.dirname(file),local);
  if(!fs.existsSync(dest))throw new Error('Broken '+attr+' in '+file+': '+target);
  links++;
 }
 // Generated body must be exactly the Markdown content on disk.
 const matches=Object.keys(data.links).filter(k=>data.links[k]===path.basename(file)&&k.endsWith('.md'));
 if(matches.length!==1)throw new Error('Ambiguous source mapping '+file);
 if(fs.readFileSync(path.resolve(path.dirname(file),matches[0]),'utf8')!==data.markdown)throw new Error('Stale embedded content '+file);
}
console.log(`PASS: ${files.length} HTML pages, ${formulas} rendered formulas, ${links} local links/assets; embedded Markdown matches sources`);
