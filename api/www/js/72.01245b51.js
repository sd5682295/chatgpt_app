"use strict";(globalThis["webpackChunkgtphtml"]=globalThis["webpackChunkgtphtml"]||[]).push([[72],{3297:(e,s,a)=>{a.d(s,{c:()=>l});var t=a(7524),o=a(1809),r=a(1650),i=a(6850),n=a(8339);const l=(0,o.Q_)("useMainLayoutData",{state:()=>({apiKey:"",validApiKey:!1,router:(0,n.tv)()}),getters:{},actions:{checkVipExpire(){const e=(0,r.m)().vipExpirationDate.getTime()-(new Date).getTime();if(e<=0)return"VIP已过期";{const s=Math.ceil(e/864e5);return`VIP还有${s}天过期`}},validateApiKey(e){const s=/^sk-[a-zA-Z0-9]{40,50}$/;return this.validApiKey=s.test(e),this.validApiKey||"输入格式不正确，请输入以 sk- 开头的 40-50 位字母或数字组成的字符串"},saveApiKey(){!1===this.validApiKey&&alert("请输入正确的apiKey");const e=localStorage.getItem("session");t.Z.post(`${(0,i.Z)().baseUrl}/saveApiKey/`,JSON.stringify({apiKey:this.apiKey,session:e}),{headers:{"Content-Type":"application/json","Access-Control-Allow-Origin":"*"}}).then((e=>{console.log("Save API Key response:",e.msg)})).catch((e=>{console.error("Save API Key error:",e)}))},handleUserClick(){console.log("用户功能还没完成")},handleUpgradeVipClick(){console.log("升级vip功能还没完成")},handleLogoutClick(){localStorage.removeItem("session"),(0,r.m)().userName="",(0,r.m)().password="",this.router.push("register-page")},handleMessageClick(){console.log("留言功能还没完成")},handleAboutUsClick(){alert("我们的信息")}}})},1650:(e,s,a)=>{a.d(s,{m:()=>p});var t=a(1809),o=a(7813),r=a(7524),i=a(8339),n=a(6850),l=a(3297);const p=(0,t.Q_)("register",{state:()=>({password:"",userName:"",vipExpirationDate:new Date,router:(0,i.tv)(),validUserName:!1,validPassWord:!1,isLoading:!1}),actions:{validateUserName(e){const s=/^[a-zA-Z0-9_]{4,20}$/;return this.validUserName=s.test(e),this.validUserName||"请使用 4 到 20 个字符的字母、数字或下划线作为用户名。"},validatePassword(e){const s=/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-_!@])[A-Za-z\d-_\!@]{8,20}$/;return this.validPassWord=s.test(e),this.validPassWord||"密码必须包含大小写字母、数字和特殊字符，长度为8-20个字符"},handleResponse(e){let s=e.data;if("string"===typeof s){s=s.replace(/NaN/g,'""').replace(/\n/g,"").trim();try{s=JSON.parse(s)}catch(a){}}return s},login(){const e=JSON.stringify({username:this.userName,password:o.V8.hashStr(this.password)});r.Z.post(`${(0,n.Z)().baseUrl}/login/`,e,{headers:{"Content-Type":"application/json","Access-Control-Allow-Origin":"*"}}).then((e=>{const s=this.handleResponse(e);if(this.isLoading=!1,0!==s.resCode)alert("用户名或者密码错误"),this.password="";else{function a(e){const s=Date.parse(e),a=new Date(s);return a}localStorage.setItem("session",s.session),this.vipExpirationDate=a(s.vipExpirationDate),(0,l.c)().apiKey=s.apiKey,this.router.push("chat-page"),console.log("注册或者创建成功")}})).catch((e=>{console.error(e)}))},usernameRule(){return[e=>!!e||"Username is required.",e=>e.length<=20||"Username must be less than or equal to 20 characters."]},passwordRule(){return[e=>!!e||"Password is required.",e=>e.length>=6||"Password must be at least 6 characters."]},getUseNameAsSession(){console.log("-1");const e=localStorage.getItem("session");if(console.log(e),e){const s=JSON.stringify({session:e}),a={"Content-Type":"application/json","Access-Control-Allow-Origin":"*"};r.Z.post(`${(0,n.Z)().baseUrl}/session/`,s,{headers:a}).then((e=>{console.log(e);const s=this.handleResponse(e);function a(e){const s=Date.parse(e),a=new Date(s);return a}0!==s.resCode?(console.log(["--aa1--",s]),this.userName="",this.password="",this.vipExpirationDate=new Date,localStorage.removeItem("session"),this.router.push("/register-page")):(console.log(["验证通过",s]),this.vipExpirationDate=a(s.vipExpirationDate),(0,l.c)().apiKey=s.apiKey,this.router.push("/chat-page"))})).catch((e=>{this.router.push("/register-page")}))}else this.userName="",this.password="",this.vipExpirationDate=new Date,localStorage.removeItem("session"),this.router.push("/register-page")}}})},6850:(e,s,a)=>{a.d(s,{Z:()=>o});var t=a(1809);const o=(0,t.Q_)("config",{state:()=>({baseUrl:"http://120.48.84.244:5000/"}),actions:{}})},1072:(e,s,a)=>{a.r(s),a.d(s,{default:()=>A});var t=a(9835),o=a(1957);const r={class:"q-gutter-md q-mt-xl q-mb-xl q-pa-md q-ma-sm",style:{"max-width":"600px"}},i=(0,t._)("h3",{style:{"font-size":"24px","border-bottom":"1px solid #ddd"}},"注册和登入",-1);function n(e,s,a,n,l,p){const d=(0,t.up)("q-input"),c=(0,t.up)("q-btn"),u=(0,t.up)("q-form");return(0,t.wg)(),(0,t.iD)("div",r,[i,(0,t.Wm)(u,{onKeyup:(0,o.D2)(e.login,["enter"])},{default:(0,t.w5)((()=>[(0,t.Wm)(d,{modelValue:e.userName,"onUpdate:modelValue":s[0]||(s[0]=s=>e.userName=s),label:"Username",type:"text",rules:[e.validateUserName],"lazy-rules":""},null,8,["modelValue","rules"]),(0,t.Wm)(d,{modelValue:e.password,"onUpdate:modelValue":s[1]||(s[1]=s=>e.password=s),label:"Password",type:"password",rules:[e.validatePassword],"lazy-rules":""},null,8,["modelValue","rules"]),(0,t.Wm)(c,{label:"Create Account",class:"q-mt-md",color:"primary",disable:!e.validUserName||!e.validPassWord||e.isLoading,loading:e.isLoading,onClick:(0,o.iM)(e.login,["prevent"])},null,8,["disable","loading","onClick"])])),_:1},8,["onKeyup"])])}var l=a(1809),p=a(1650);const d=(0,t.aZ)({name:"registerPage",computed:Object.assign({},(0,l.Ah)(p.m,["password","userName","validUserName","validPassWord","isLoading"])),methods:Object.assign({},(0,l.nv)(p.m,["login","validatePassword","validateUserName"]))});var c=a(1639),u=a(8326),h=a(4925),m=a(7065),g=a(4458),v=a(9984),y=a.n(v);const w=(0,c.Z)(d,[["render",n]]),A=w;y()(d,"components",{QForm:u.Z,QInput:h.Z,QBtn:m.Z,QCard:g.Z})}}]);