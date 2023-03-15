"use strict";(globalThis["webpackChunkgtphtml"]=globalThis["webpackChunkgtphtml"]||[]).push([[568],{3297:(e,s,t)=>{t.d(s,{c:()=>l});var a=t(7524),o=t(1809),n=t(1650),r=t(6850),i=t(8339);const l=(0,o.Q_)("useMainLayoutData",{state:()=>({apiKey:"",validApiKey:!1,router:(0,i.tv)()}),getters:{},actions:{checkVipExpire(){const e=(0,n.m)().vipExpirationDate.getTime()-(new Date).getTime();if(e<=0)return"VIP已过期";{const s=Math.ceil(e/864e5);return`VIP还有${s}天过期`}},validateApiKey(e){const s=/^sk-[a-zA-Z0-9]{40,50}$/;return this.validApiKey=s.test(e),this.validApiKey||"输入格式不正确，请输入以 sk- 开头的 40-50 位字母或数字组成的字符串"},saveApiKey(){!1===this.validApiKey&&alert("请输入正确的apiKey");const e=localStorage.getItem("session");a.Z.post(`${(0,r.Z)().baseUrl}/saveApiKey/`,JSON.stringify({apiKey:this.apiKey,session:e}),{headers:{"Content-Type":"application/json","Access-Control-Allow-Origin":"*"}}).then((e=>{console.log("Save API Key response:",e.msg)})).catch((e=>{console.error("Save API Key error:",e)}))},handleUserClick(){console.log("用户功能还没完成")},handleUpgradeVipClick(){console.log("升级vip功能还没完成")},handleLogoutClick(){localStorage.removeItem("session"),(0,n.m)().userName="",(0,n.m)().password="",this.router.push("register-page")},handleMessageClick(){console.log("留言功能还没完成")},handleAboutUsClick(){alert("我们的信息")}}})},1650:(e,s,t)=>{t.d(s,{m:()=>c});var a=t(1809),o=t(7813),n=t(7524),r=t(8339),i=t(6850),l=t(3297);const c=(0,a.Q_)("register",{state:()=>({password:"",userName:"",vipExpirationDate:new Date,router:(0,r.tv)(),validUserName:!1,validPassWord:!1,isLoading:!1}),actions:{validateUserName(e){const s=/^[a-zA-Z0-9_]{4,20}$/;return this.validUserName=s.test(e),this.validUserName||"请使用 4 到 20 个字符的字母、数字或下划线作为用户名。"},validatePassword(e){const s=/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-_!@])[A-Za-z\d-_\!@]{8,20}$/;return this.validPassWord=s.test(e),this.validPassWord||"密码必须包含大小写字母、数字和特殊字符，长度为8-20个字符"},handleResponse(e){let s=e.data;if("string"===typeof s){s=s.replace(/NaN/g,'""').replace(/\n/g,"").trim();try{s=JSON.parse(s)}catch(t){}}return s},login(){const e=JSON.stringify({username:this.userName,password:o.V8.hashStr(this.password)});n.Z.post(`${(0,i.Z)().baseUrl}/login/`,e,{headers:{"Content-Type":"application/json","Access-Control-Allow-Origin":"*"}}).then((e=>{const s=this.handleResponse(e);if(this.isLoading=!1,0!==s.resCode)alert("用户名或者密码错误"),this.password="";else{function t(e){const s=Date.parse(e),t=new Date(s);return t}localStorage.setItem("session",s.session),this.vipExpirationDate=t(s.vipExpirationDate),(0,l.c)().apiKey=s.apiKey,this.router.push("chat-page"),console.log("注册或者创建成功")}})).catch((e=>{console.error(e)}))},usernameRule(){return[e=>!!e||"Username is required.",e=>e.length<=20||"Username must be less than or equal to 20 characters."]},passwordRule(){return[e=>!!e||"Password is required.",e=>e.length>=6||"Password must be at least 6 characters."]},getUseNameAsSession(){console.log("-1");const e=localStorage.getItem("session");if(console.log(e),e){const s=JSON.stringify({session:e}),t={"Content-Type":"application/json","Access-Control-Allow-Origin":"*"};n.Z.post(`${(0,i.Z)().baseUrl}/session/`,s,{headers:t}).then((e=>{console.log(e);const s=this.handleResponse(e);function t(e){const s=Date.parse(e),t=new Date(s);return t}0!==s.resCode?(console.log(["--aa1--",s]),this.userName="",this.password="",this.vipExpirationDate=new Date,localStorage.removeItem("session"),this.router.push("/register-page")):(console.log(["验证通过",s]),this.vipExpirationDate=t(s.vipExpirationDate),(0,l.c)().apiKey=s.apiKey,this.router.push("/chat-page"))})).catch((e=>{this.router.push("/register-page")}))}else this.userName="",this.password="",this.vipExpirationDate=new Date,localStorage.removeItem("session"),this.router.push("/register-page")}}})},6850:(e,s,t)=>{t.d(s,{Z:()=>o});var a=t(1809);const o=(0,a.Q_)("config",{state:()=>({baseUrl:"http://120.48.84.244:5000/"}),actions:{}})},5568:(e,s,t)=>{t.r(s),t.d(s,{default:()=>D});var a=t(9835);const o={class:"chat-container"},n={class:"chat-messages"},r={class:"q-pa-md row justify-center"},i={style:{width:"100%","max-width":"600px"}},l={class:"chat-form"};function c(e,s,t,c,p,h){const g=(0,a.up)("q-chat-message"),d=(0,a.up)("el-input"),u=(0,a.up)("el-button");return(0,a.wg)(),(0,a.iD)("div",o,[(0,a._)("div",n,[(0,a._)("div",r,[(0,a._)("div",i,[((0,a.wg)(!0),(0,a.iD)(a.HY,null,(0,a.Ko)(e.messages,((e,s)=>((0,a.wg)(),(0,a.j4)(g,{key:s,text:e.content,sent:e.sent,name:e.author,avatar:e.avatar},null,8,["text","sent","name","avatar"])))),128))])])]),(0,a._)("div",l,[(0,a.Wm)(d,{modelValue:e.newMessage,"onUpdate:modelValue":s[0]||(s[0]=s=>e.newMessage=s),placeholder:"Type your message"},null,8,["modelValue"]),(0,a.Wm)(u,{type:"primary",onClick:e.sendMessage},{default:(0,a.w5)((()=>[(0,a.Uk)("Send")])),_:1},8,["onClick"])])])}var p=t(1809),h=t(7524),g=t(1650),d=t(3297),u=t(6850);const m=(0,p.Q_)("chatPageData",{state:()=>({messages:[{author:"user",content:["hello world"],type:"user",sent:!1,avatar:"https://cdn.quasar.dev/img/avatar1.jpg"},{author:"System",content:["Welcome to Facebook Chat Room!"],type:"system",sent:!0,avatar:"https://cdn.quasar.dev/img/avatar1.jpg"}],newMessage:""}),actions:{sendMessage(){const e=localStorage.getItem("session");if(""===this.newMessage)return void alert("请输入信息");this.messages.push({author:(0,g.m)().userName,content:[this.newMessage],type:"user",sent:!0,avatar:"https://cdn.quasar.dev/img/avatar1.jpg"});const s=JSON.stringify({newMessage:this.newMessage,session:e,apiKey:(0,d.c)().apiKey});h.Z.post(`${(0,u.Z)().baseUrl}/sent/`,s,{headers:{"Content-Type":"application/json","Access-Control-Allow-Origin":"*"}}).then((e=>{console.log(["sendMessage",e]),0===e.data.resCode?this.messages.push({author:"chatgpt",content:[e.data.resMessage],type:"AI",sent:!1,avatar:"https://tse2-mm.cn.bing.net/th/id/OIP-C.cKsck1yFTO7rGVxOO284PQHaJ-?w=139&h=187&c=7&r=0&o=5&dpr=1.3&pid=1.7"}):2===e.data.resCode&&this.messages.push({author:"chatgpt",content:["VIP已过期，请续费！"],type:"AI",sent:!1,avatar:"https://tse2-mm.cn.bing.net/th/id/OIP-C.cKsck1yFTO7rGVxOO284PQHaJ-?w=139&h=187&c=7&r=0&o=5&dpr=1.3&pid=1.7"}),this.newMessage=""})).catch((e=>{console.error(e)}))}}}),v=(0,a.aZ)({name:"chatPage",computed:{...(0,p.Ah)(g.m,["password","userName"]),...(0,p.Ah)(m,["messages","newMessage"])},methods:{...(0,p.nv)(g.m,["onSubmit"]),...(0,p.nv)(m,["sendMessage"])}});var y=t(1639),w=t(396),A=t(9984),C=t.n(A);const K=(0,y.Z)(v,[["render",c]]),D=K;C()(v,"components",{QChatMessage:w.Z})}}]);