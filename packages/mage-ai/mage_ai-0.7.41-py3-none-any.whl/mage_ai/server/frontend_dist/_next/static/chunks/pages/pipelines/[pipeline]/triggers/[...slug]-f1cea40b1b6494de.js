(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[643],{2850:function(e,n,t){"use strict";t.d(n,{M:function(){return c}});var r=t(9518),i=t(23831),l=t(3055),c=r.default.div.withConfig({displayName:"indexstyle__BeforeStyle",componentId:"sc-12ee2ib-0"})(["min-height:calc(100vh - ","px);",""],l.Mz,(function(e){return"\n    border-left: 1px solid ".concat((e.theme.borders||i.Z.borders).medium,";\n  ")}))},56681:function(e,n,t){"use strict";t.d(n,{G:function(){return b},Z:function(){return Z}});var r=t(12757),i=t(82394),l=t(26304),c=t(32316),o=t(22673),s=t(86532),u=t(86673),a=t(19711),d=t(17903),p=t(49125),h=t(19395),f=t(28598),m=["height","heightOffset","pipeline","selectedRun","selectedTab","setSelectedTab"];function g(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function v(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?g(Object(t),!0).forEach((function(n){(0,i.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):g(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}var j={uuid:"Run details"},x={uuid:"Dependency tree"},b=[x,j];function Z(e){var n=e.height,t=e.heightOffset,i=e.pipeline,g=e.selectedRun,Z=e.selectedTab,y=e.setSelectedTab,O=v({},(0,l.Z)(e,m));g?O.blockStatus=(0,h.IJ)(null===g||void 0===g?void 0:g.block_runs):O.noStatus=!0;var _=(null===g||void 0===g?void 0:g.variables)||{};null!==g&&void 0!==g&&g.event_variables&&(_.event=g.event_variables);var P=[];_&&JSON.stringify(_,null,2).split("\n").forEach((function(e){P.push("    ".concat(e))}));var S=g&&[["Run ID",null===g||void 0===g?void 0:g.id],["Variables",(0,f.jsx)(o.Z,{language:"json",small:!0,source:P.join("\n")})]],w=g&&(0,f.jsx)(u.Z,{pb:p.cd,px:p.cd,children:(0,f.jsx)(d.Z,{alignTop:!0,columnFlex:[null,1],columnMaxWidth:function(e){return 1===e?"100px":null},rows:S.map((function(e){var n=(0,r.Z)(e,2),t=n[0],i=n[1];return[(0,f.jsx)(a.ZP,{monospace:!0,muted:!0,children:t}),(0,f.jsx)(a.ZP,{monospace:!0,textOverflow:!0,children:i})]})),uuid:"LogDetail"})}),I=Z&&y;return(0,f.jsxs)(f.Fragment,{children:[I&&(0,f.jsx)(u.Z,{py:p.cd,children:(0,f.jsx)(c.Z,{onClickTab:y,selectedTabUUID:null===Z||void 0===Z?void 0:Z.uuid,tabs:b})}),(!I||x.uuid===(null===Z||void 0===Z?void 0:Z.uuid))&&(0,f.jsx)(s.Z,v(v({},O),{},{height:n,heightOffset:(t||0)+(I?76:0),pipeline:i})),j.uuid===(null===Z||void 0===Z?void 0:Z.uuid)&&w]})}},18025:function(e,n,t){"use strict";t.d(n,{J:function(){return s},U:function(){return o}});var r=t(9518),i=t(23831),l=t(73942),c=t(49125),o=r.default.div.withConfig({displayName:"indexstyle__CardStyle",componentId:"sc-m7tlau-0"})(["border-radius:","px;border-style:solid;border-width:2px;height:","px;margin-right:","px;padding:","px;width:","px;"," ",""],l.TR,14*c.iI,c.cd*c.iI,c.cd*c.iI,40*c.iI,(function(e){return!e.selected&&"\n    border-color: ".concat((e.theme.borders||i.Z.borders).light,";\n  ")}),(function(e){return e.selected&&"\n    border-color: ".concat((e.theme.interactive||i.Z.interactive).linkPrimary,";\n  ")})),s=r.default.div.withConfig({displayName:"indexstyle__DateSelectionContainer",componentId:"sc-m7tlau-1"})(["border-radius:","px;padding:","px;"," "," ",""],l.n_,c.tr,(function(e){return"\n    background-color: ".concat((e.theme.interactive||i.Z.interactive).defaultBackground,";\n  ")}),(function(e){return e.absolute&&"\n    position: absolute;\n    z-index: 2;\n    right: 0;\n    top: ".concat(2.5*c.iI,"px;\n  ")}),(function(e){return e.topPosition&&"\n    top: -".concat(42*c.iI,"px;\n  ")}))},2713:function(e,n,t){"use strict";var r=t(82394),i=t(44495),l=t(67971),c=t(55378),o=t(86673),s=t(19711),u=t(18025),a=t(49125),d=t(24224),p=t(28598);function h(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function f(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?h(Object(t),!0).forEach((function(n){(0,r.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):h(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}n.Z=function(e){var n=e.selectedDate,t=e.selectedTime,r=e.setSelectedDate,h=e.setSelectedTime,m=e.topPosition;return(0,p.jsxs)(u.J,{absolute:!0,topPosition:m,children:[(0,p.jsx)(i.ZP,{onChange:r,value:n}),(0,p.jsx)(o.Z,{mb:2}),(0,p.jsxs)(l.Z,{alignItems:"center",children:[(0,p.jsx)(s.ZP,{default:!0,large:!0,children:"Time (UTC):"}),(0,p.jsx)(o.Z,{pr:2}),(0,p.jsx)(c.Z,{compact:!0,monospace:!0,onChange:function(e){e.preventDefault(),h((function(n){return f(f({},n),{},{hour:e.target.value})}))},paddingRight:5*a.iI,placeholder:"HH",value:null===t||void 0===t?void 0:t.hour,children:(0,d.m5)(24,0).map((function(e){return String(e).padStart(2,"0")})).map((function(e){return(0,p.jsx)("option",{value:e,children:e},"hour_".concat(e))}))}),(0,p.jsx)(o.Z,{px:1,children:(0,p.jsx)(s.ZP,{bold:!0,large:!0,children:":"})}),(0,p.jsx)(c.Z,{compact:!0,monospace:!0,onChange:function(e){e.preventDefault(),h((function(n){return f(f({},n),{},{minute:e.target.value})}))},paddingRight:5*a.iI,placeholder:"MM",value:null===t||void 0===t?void 0:t.minute,children:(0,d.m5)(60,0).map((function(e){return String(e).padStart(2,"0")})).map((function(e){return(0,p.jsx)("option",{value:e,children:e},"minute_".concat(e))}))})]})]})}},82944:function(e,n,t){"use strict";var r=t(82394),i=t(91835),l=t(82684),c=t(9518),o=t(69898),s=t(28598);function u(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function a(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?u(Object(t),!0).forEach((function(n){(0,r.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):u(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}var d=c.default.input.withConfig({displayName:"TextInput__TextInputStyle",componentId:"sc-1ii4qtc-0"})(["",""],o.p),p=function(e,n){var t=(0,i.Z)({},e);return(0,s.jsx)(o.Z,a(a({},t),{},{input:(0,s.jsx)(d,a({},t)),ref:n}))};n.Z=l.forwardRef(p)},54183:function(e,n,t){"use strict";t.r(n),t.d(n,{default:function(){return Se}});var r,i=t(12757),l=t(77837),c=t(82394),o=t(38860),s=t.n(o),u=t(82684),a=t(83455),d=t(34376),p=t(60328),h=t(34744),f=t(67971),m=t(87372),g=t(51099),v=t(38965),j=t(97496),x=t(47409),b=t(93348),Z=t(55378),y=t(86673),O=t(17903),_=t(19711),P=t(41374),S=t(56681),w=t(2850),I=t(10503),E=t(49125),T=t(59920),k=t(24224);!function(e){e.AWS="aws_event"}(r||(r={}));var C=[{label:function(){return"AWS"},uuid:r.AWS}],D=(0,k.HK)(C,(function(e){return e.uuid})),M=t(66050),N=t(58122),A=t(19395),U=t(33766),R=t(7715),F=t(96510),H=t(66653),z=t(59e3),q=t(28598);function V(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function L(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?V(Object(t),!0).forEach((function(n){(0,c.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):V(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}var W=function(e){var n=e.fetchPipelineSchedule,t=e.pipeline,r=e.pipelineSchedule,l=e.variables,c=(0,d.useRouter)(),o=(t||{}).uuid,s=r||{},k=s.id,C=s.event_matchers,V=s.name,W=s.schedule_interval,X=s.schedule_type,J=s.sla,G=s.start_time,B=s.status,K=s.variables,Y=void 0===K?{}:K,Q=(0,z.iV)(),$={_limit:30,_offset:30*(null!==Q&&void 0!==Q&&Q.page?Q.page:0)};null!==Q&&void 0!==Q&&Q.status&&($.status=Q.status);var ee=P.ZP.pipeline_runs.pipeline_schedules.list(k,$,{refreshInterval:3e3,revalidateOnFocus:!0}),ne=ee.data,te=ee.mutate,re=(0,u.useMemo)((function(){return(null===ne||void 0===ne?void 0:ne.pipeline_runs)||[]}),[ne]),ie=(0,u.useMemo)((function(){return(null===ne||void 0===ne?void 0:ne.total_count)||[]}),[ne]),le=(0,u.useState)(null),ce=le[0],oe=le[1],se=(0,u.useMemo)((function(){var e=null!==Q&&void 0!==Q&&Q.page?Q.page:0;return(0,q.jsxs)(q.Fragment,{children:[(0,q.jsx)(j.Z,{fetchPipelineRuns:te,onClickRow:function(e){return oe((function(n){var t=re[e];return(null===n||void 0===n?void 0:n.id)!==t.id?t:null}))},pipelineRuns:re,selectedRun:ce}),(0,q.jsx)(y.Z,{p:2,children:(0,q.jsx)(g.Z,{page:Number(e),maxPages:9,onUpdate:function(e){var n=Number(e),t=L(L({},Q),{},{page:n>=0?n:0});c.push("/pipelines/[pipeline]/triggers/[...slug]","/pipelines/".concat(o,"/triggers/").concat(k,"?").concat((0,z.uM)(t)))},totalPages:Math.ceil(ie/30)})})]})}),[te,t,re,ce]),ue=(0,u.useState)(S.G[0]),ae=ue[0],de=ue[1],pe=(0,a.Db)((function(e){return P.ZP.pipeline_schedules.useUpdate(e.id)({pipeline_schedule:e})}),{onSuccess:function(e){return(0,F.wD)(e,{callback:function(){n()},onErrorCallback:function(e){var n=e.error,t=n.errors,r=n.message;console.log(t,r)}})}}),he=(0,i.Z)(pe,2),fe=he[0],me=he[1].isLoading,ge=(0,u.useMemo)((function(){return b.fq.ACTIVE===B}),[B]),ve=(0,u.useMemo)((function(){var e,n={default:!0,size:1.5*E.iI},t=[[(0,q.jsxs)(f.Z,{alignItems:"center",children:[(0,q.jsx)(I.VW,L({},n)),(0,q.jsx)(y.Z,{mr:1}),(0,q.jsx)(_.ZP,{default:!0,children:"Trigger type"})]},"trigger_type_label"),(0,q.jsx)(_.ZP,{monospace:!0,children:null===(e=b.Z4[X])||void 0===e?void 0:e.call(b.Z4)},"trigger_type")],[(0,q.jsxs)(f.Z,{alignItems:"center",children:[(0,q.jsx)(I.rs,L({},n)),(0,q.jsx)(y.Z,{mr:1}),(0,q.jsx)(_.ZP,{default:!0,children:"Status"})]},"trigger_status_label"),(0,q.jsx)(_.ZP,{danger:!ge,monospace:!0,success:ge,children:B},"trigger_status")]];if(J){var r=(0,A.gU)(J),i=r.time,l=r.unit,c=1===i?l:"".concat(l,"s");t.push([(0,q.jsxs)(f.Z,{alignItems:"center",children:[(0,q.jsx)(I.kI,L({},n)),(0,q.jsx)(y.Z,{mr:1}),(0,q.jsx)(_.ZP,{default:!0,children:"SLA"})]},"trigger_sla_label"),(0,q.jsx)(_.ZP,{monospace:!0,children:"".concat(i," ").concat(c)},"trigger_sla")])}return W&&t.push([(0,q.jsxs)(f.Z,{alignItems:"center",children:[(0,q.jsx)(I.Pf,L({},n)),(0,q.jsx)(y.Z,{mr:1}),(0,q.jsx)(_.ZP,{default:!0,children:"Frequency"})]},"trigger_frequency_label"),(0,q.jsx)(_.ZP,{monospace:!0,children:W.replace("@","")},"trigger_frequency")]),G&&t.push([(0,q.jsxs)(f.Z,{alignItems:"center",children:[(0,q.jsx)(I.aw,L({},n)),(0,q.jsx)(y.Z,{mr:1}),(0,q.jsx)(_.ZP,{default:!0,children:"Start date"})]},"trigger_start_date_label"),(0,q.jsx)(_.ZP,{monospace:!0,children:G},"trigger_start_date")]),(0,q.jsx)(O.Z,{columnFlex:[null,1],rows:t})}),[ge,W,J,G,X]),je=(0,u.useMemo)((function(){return Y||{}}),[Y]),xe=(0,u.useMemo)((function(){var e,n=[];return(0,R.Qr)(je)?n=(0,N.wx)(l,(function(e){return"global"===e.uuid})):Object.entries(je).forEach((function(e){var t=(0,i.Z)(e,2),r=t[0],l=t[1];n.push({uuid:r,value:(0,N.FS)(l)})})),"undefined"!==typeof(n=(0,N.JZ)(n||[],X))&&null!==(e=n)&&void 0!==e&&e.length?(0,q.jsx)(O.Z,{columnFlex:[null,1],rows:n.map((function(e){var n=e.uuid,t=e.value;return[(0,q.jsx)(_.ZP,{default:!0,monospace:!0,small:!0,children:n},"settings_variable_label_".concat(n)),(0,q.jsx)(_.ZP,{monospace:!0,small:!0,children:t},"settings_variable_".concat(n))]}))}):null}),[X,Y,l]),be=(0,u.useMemo)((function(){return(0,q.jsx)(O.Z,{columnFlex:[null,1],columns:[{uuid:"Provider"},{uuid:"Event"}],rows:null===C||void 0===C?void 0:C.map((function(e,n){var t=e.event_type,r=e.name;return[(0,q.jsx)(_.ZP,{default:!0,monospace:!0,children:D[t].label()},"".concat(t,"_").concat(n,"_label")),(0,q.jsx)(_.ZP,{monospace:!0,children:r},"".concat(t,"_").concat(n,"_name"))]}))})}),[C]);return(0,q.jsxs)(v.Z,{afterHidden:!ce,before:(0,q.jsxs)(w.M,{children:[(0,q.jsxs)(y.Z,{mb:E.HN,pt:E.cd,px:E.cd,children:[(0,q.jsxs)(y.Z,{mb:E.cd,children:[b.Xm.TIME===X&&(0,q.jsx)(I.kO,{size:5*E.iI}),b.Xm.EVENT===X&&(0,q.jsx)(I.Jp,{size:5*E.iI}),!X&&(0,q.jsx)(I.VW,{size:5*E.iI})]}),(0,q.jsx)(m.Z,{children:V})]}),(0,q.jsx)(y.Z,{px:E.cd,children:(0,q.jsx)(m.Z,{level:5,children:"Settings"})}),(0,q.jsx)(h.Z,{light:!0,mt:1,short:!0}),ve,(null===C||void 0===C?void 0:C.length)>=1&&(0,q.jsxs)(y.Z,{my:E.HN,children:[(0,q.jsx)(y.Z,{px:E.cd,children:(0,q.jsx)(m.Z,{level:5,children:"Events"})}),(0,q.jsx)(h.Z,{light:!0,mt:1,short:!0}),be]}),xe&&(0,q.jsxs)(y.Z,{my:E.HN,children:[(0,q.jsx)(y.Z,{px:E.cd,children:(0,q.jsx)(m.Z,{level:5,children:"Runtime variables"})}),(0,q.jsx)(h.Z,{light:!0,mt:1,short:!0}),xe]})]}),beforeWidth:34*E.iI,breadcrumbs:[{label:function(){return"Triggers"},linkProps:{as:"/pipelines/".concat(o,"/triggers"),href:"/pipelines/[pipeline]/triggers"}},{label:function(){return V},linkProps:{as:"/pipelines/".concat(o,"/triggers/").concat(k),href:"/pipelines/[pipeline]/triggers/[...slug]"}}],buildSidekick:function(e){return(0,S.Z)(L(L({},e),{},{selectedRun:ce,selectedTab:ae,setSelectedTab:de}))},pageName:T.M.TRIGGERS,pipeline:t,subheader:(0,q.jsxs)(f.Z,{alignItems:"center",children:[(0,q.jsx)(p.Z,{beforeIcon:ge?(0,q.jsx)(I.dz,{size:2*E.iI}):(0,q.jsx)(I.Py,{inverted:!0,size:2*E.iI}),danger:ge,loading:me,onClick:function(e){(0,H.j)(e),fe({id:k,status:ge?b.fq.INACTIVE:b.fq.ACTIVE})},outline:!0,success:!ge,children:ge?"Pause trigger":"Start trigger"}),(0,q.jsx)(y.Z,{mr:E.cd}),(0,q.jsx)(p.Z,{linkProps:{as:"/pipelines/".concat(o,"/triggers/").concat(k,"/edit"),href:"/pipelines/[pipeline]/triggers/[...slug]"},noHoverUnderline:!0,outline:!0,sameColorAsText:!0,children:"Edit trigger"}),(0,q.jsx)(y.Z,{mr:E.cd}),(0,q.jsxs)(Z.Z,{compact:!0,defaultColor:!0,onChange:function(e){e.preventDefault(),"all"===e.target.value?c.push("/pipelines/[pipeline]/triggers/[...slug]","/pipelines/".concat(o,"/triggers/").concat(k)):(0,U.u)({page:0,status:e.target.value})},paddingRight:4*E.iI,placeholder:"Select run status",value:(null===Q||void 0===Q?void 0:Q.status)||"all",children:[(0,q.jsx)("option",{value:"all",children:"All statuses"},"all_statuses"),Object.values(M.V).map((function(e){return(0,q.jsx)("option",{value:e,children:x.D[e]},e)}))]})]}),title:function(){return V},uuid:"triggers/detail",children:[(0,q.jsx)(y.Z,{mt:E.cd,px:E.cd,children:(0,q.jsx)(m.Z,{level:5,children:"Runs for this trigger"})}),(0,q.jsx)(h.Z,{light:!0,mt:E.cd,short:!0}),se]})},X=t(77555),J=t(21764),G=t(2713),B=t(47999),K=t(22673),Y=t(65730),Q=t(28358),$=t(93461),ee=t(10919),ne=t(26304),te=t(9518),re=t(23831),ie=t(2005),le=t(31012),ce=["children","large","lineHeight","ordered"];function oe(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function se(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?oe(Object(t),!0).forEach((function(n){(0,c.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):oe(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}var ue=(0,te.css)([""," "," "," "," "," "," "," "," "," ",""],(function(e){return!e.muted&&"\n    color: ".concat((e.theme.content||re.Z.content).default,";\n  ")}),(function(e){return e.muted&&"\n    color: ".concat((e.theme.content||re.Z.content).muted,";\n  ")}),(function(e){return e.inverted&&"\n    color: ".concat((e.theme.content||re.Z.content).inverted,";\n  ")}),(function(e){return e.color&&"\n    color: ".concat(e.color,";\n  ")}),(function(e){return!e.monospace&&"\n    font-family: ".concat(ie.ry,";\n  ")}),(function(e){return e.monospace&&"\n    font-family: ".concat(ie.Vp,";\n  ")}),(function(e){return e.large&&"\n    ".concat(le.x_,"\n  ")}),(function(e){return!e.large&&!e.small&&"\n    ".concat(le.i3,"\n  ")}),(function(e){return e.small&&"\n    ".concat(le.J5,"\n  ")}),(function(e){return e.lineHeight&&"\n    line-height: ".concat(e.lineHeight,"px !important;\n  ")})),ae=te.default.ul.withConfig({displayName:"List__UnorderedListStyle",componentId:"sc-1f6yhbi-0"})(["",""],ue),de=te.default.ol.withConfig({displayName:"List__OrderedListStyle",componentId:"sc-1f6yhbi-1"})(["",""],ue),pe=te.default.li.withConfig({displayName:"List__ListItemStyle",componentId:"sc-1f6yhbi-2"})(["",""],(function(e){return e.large&&e.marginTop&&"\n    margin-top: ".concat(1*E.iI,"px;\n  ")}));var he=function(e){var n=e.children,t=e.large,r=e.lineHeight,i=e.ordered,l=(0,ne.Z)(e,ce),c=i?de:ae;return(0,q.jsx)(c,se(se({large:t,lineHeight:r},l),{},{children:u.Children.map(n,(function(e,n){return(0,q.jsx)(pe,se(se({large:t,marginTop:n>=1},l),{},{children:u.cloneElement(e)}),e.props.key)}))}))},fe=t(98781),me=t(82944),ge=t(70902),ve=t(18025);function je(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function xe(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?je(Object(t),!0).forEach((function(n){(0,c.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):je(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}var be=function(e){var n=[{description:function(){return"This pipeline will run continuously on an interval or just once."},label:function(){return"Schedule"},uuid:b.Xm.TIME},{description:function(){return"This pipeline will run when a specific event occurs."},label:function(){return"Event"},uuid:b.Xm.EVENT},{description:function(){return"Run this pipeline when you make an API call."},label:function(){return"API"},uuid:b.Xm.API}];return e?n.slice(0,1):n};var Ze=function(e){var n=e.fetchPipelineSchedule,t=e.pipeline,r=e.pipelineSchedule,l=e.variables,o=(0,d.useRouter)(),s=null===t||void 0===t?void 0:t.uuid,g=null===r||void 0===r?void 0:r.id,j=(null===t||void 0===t?void 0:t.type)===fe.q.STREAMING,x=(0,u.useState)(null),S=x[0],w=x[1],D=(0,u.useState)([]),M=D[0],U=D[1],H=(0,u.useState)(!1),z=H[0],V=H[1],L=(0,u.useState)(!1),W=L[0],ne=L[1],te=(0,u.useState)({}),re=te[0],ie=te[1],le=(0,u.useState)(r),ce=le[0],oe=le[1],se=(0,u.useState)(!1),ue=se[0],ae=se[1],de=(0,u.useState)(null),pe=de[0],je=de[1],Ze=(0,u.useMemo)((function(){return(0,N.wx)(l,(function(e){return"global"===e.uuid}))}),[l]),ye=ce||{},Oe=ye.name,_e=ye.schedule_interval,Pe=ye.schedule_type,Se=ye.sla,we=ye.start_time,Ie=ye.variables,Ee=void 0===Ie?{}:Ie,Te=(0,u.useState)(null),ke=Te[0],Ce=Te[1],De=(0,u.useState)({hour:"00",minute:"00"}),Me=De[0],Ne=De[1],Ae=P.ZP.event_rules.detail("aws").data,Ue=(0,u.useMemo)((function(){return(null===Ae||void 0===Ae?void 0:Ae.event_rules)||[]}),[Ae]),Re=(0,u.useMemo)((function(){return(0,k.HK)(Ue,(function(e){return e.name}))}),[Ue]),Fe=(0,a.Db)(P.ZP.pipeline_schedules.useUpdate(g),{onSuccess:function(e){return(0,F.wD)(e,{callback:function(){n(),o.push("/pipelines/[pipeline]/triggers/[...slug]","/pipelines/".concat(s,"/triggers/").concat(g))},onErrorCallback:function(e,n){return w({errors:n,response:e})}})}}),He=(0,i.Z)(Fe,2),ze=He[0],qe=He[1].isLoading,Ve=(0,u.useMemo)((function(){return Ee||{}}),[Ee]);(0,u.useEffect)((function(){if(we){var e=we.split(" ")[1];Ce((0,A.eI)(we)),Ne({hour:e.substring(0,2),minute:e.substring(3,5)})}else{var n=new Date;Ce(n),Ne({hour:String(n.getUTCHours()).padStart(2,"0"),minute:String(n.getUTCMinutes()).padStart(2,"0")})}}),[we]),(0,u.useEffect)((function(){Ve&&Object.keys(Ve).length>0&&V(!0)}),[Ve]),(0,u.useEffect)((function(){ie(z?null===Ze||void 0===Ze?void 0:Ze.reduce((function(e,n){var t=n.uuid,r=n.value;return xe(xe({},e),{},(0,c.Z)({},t,Ve[t]||r))}),{}):null)}),[Ze,z]),(0,u.useEffect)((function(){if(r&&(U(r.event_matchers),We?(oe(xe(xe({},r),{},{schedule_interval:"custom"})),je(_e)):oe(j?xe(xe({},r),{},{schedule_interval:b.U5.ONCE}):r),r.sla)){ne(!0);var e=(0,A.gU)(Se),n=e.time,t=e.unit;oe((function(e){return xe(xe({},e),{},{slaAmount:n,slaUnit:t})}))}}),[r]);var Le=(0,u.useCallback)((function(){var e=xe(xe({},(0,R.GL)(ce,["name","schedule_type"])),{},{event_matchers:[],schedule_interval:null,start_time:null,variables:(0,N.e7)(re)});if(b.Xm.EVENT===ce.schedule_type?e.event_matchers=M:(e.schedule_interval=We?pe:ce.schedule_interval,e.start_time=ke&&null!==Me&&void 0!==Me&&Me.hour&&null!==Me&&void 0!==Me&&Me.minute?"".concat(ke.toISOString().split("T")[0]," ").concat(null===Me||void 0===Me?void 0:Me.hour,":").concat(null===Me||void 0===Me?void 0:Me.minute,":00"):null),W){var n=null===ce||void 0===ce?void 0:ce.slaAmount,t=null===ce||void 0===ce?void 0:ce.slaUnit;if(!n||isNaN(n)||!t)return void J.Am.error("Please enter a valid SLA",{position:J.Am.POSITION.BOTTOM_RIGHT,toastId:"sla_error"});e.sla=(0,A.vJ)(n,t)}else null!==r&&void 0!==r&&r.sla&&(e.sla=0);ze({pipeline_schedule:e})}),[pe,ke,W,M,r,re,ce,Me,ze]),We=(0,u.useMemo)((function(){return _e&&!Object.values(b.U5).includes(_e)}),[_e]),Xe=(0,u.useMemo)((function(){var e=[[(0,q.jsxs)(f.Z,{alignItems:"center",children:[(0,q.jsx)(I.KJ,{default:!0,size:1.5*E.iI}),(0,q.jsx)(y.Z,{mr:1}),(0,q.jsx)(_.ZP,{default:!0,children:"Trigger name"})]},"trigger_name_detail"),(0,q.jsx)(me.Z,{monospace:!0,onChange:function(e){e.preventDefault(),oe((function(n){return xe(xe({},n),{},{name:e.target.value})}))},placeholder:"Name this trigger",value:Oe},"trigger_name_input_detail")],[(0,q.jsxs)(f.Z,{alignItems:"center",children:[(0,q.jsx)(I.Pf,{default:!0,size:1.5*E.iI}),(0,q.jsx)(y.Z,{mr:1}),(0,q.jsx)(_.ZP,{default:!0,children:"Frequency"})]},"frequency"),(0,q.jsxs)(Z.Z,{monospace:!0,onChange:function(e){e.preventDefault();var n=e.target.value;oe((function(e){return xe(xe({},e),{},{schedule_interval:n})}))},placeholder:"Choose the frequency to run",value:_e,children:[!_e&&(0,q.jsx)("option",{value:""}),Object.values(b.U5).map((function(e){return(0,q.jsx)("option",{value:e,children:e.substring(1)},e)})),(0,q.jsx)("option",{value:"custom",children:"custom"},"custom")]},"frequency_input")],[(0,q.jsxs)(f.Z,{alignItems:"center",children:[(0,q.jsx)(I.aw,{default:!0,size:1.5*E.iI}),(0,q.jsx)(y.Z,{mr:1}),(0,q.jsx)(_.ZP,{default:!0,children:"Start date and time"})]},"start_time"),(0,q.jsxs)("div",{style:{minHeight:"".concat(5.75*E.iI,"px")},children:[!ue&&(0,q.jsx)(me.Z,{monospace:!0,onClick:function(){return ae((function(e){return!e}))},placeholder:"YYYY-MM-DD HH:MM",value:ke?"".concat(ke.toISOString().split("T")[0]," ").concat(null===Me||void 0===Me?void 0:Me.hour,":").concat(null===Me||void 0===Me?void 0:Me.minute):""}),(0,q.jsx)("div",{style:{width:"400px"},children:(0,q.jsx)(B.Z,{disableEscape:!0,onClickOutside:function(){return ae(!1)},open:ue,style:{position:"relative"},children:(0,q.jsx)(G.Z,{selectedDate:ke,selectedTime:Me,setSelectedDate:Ce,setSelectedTime:Ne,topPosition:!0})})})]},"start_time_input")]];return j&&e.splice(1,1),We&&e.splice(2,0,[(0,q.jsxs)(f.Z,{alignItems:"center",children:[(0,q.jsx)(I.EK,{default:!0,size:1.5*E.iI}),(0,q.jsx)(y.Z,{mr:1}),(0,q.jsx)(_.ZP,{default:!0,children:"Cron expression"})]},"cron_expression"),(0,q.jsx)(me.Z,{monospace:!0,onChange:function(e){e.preventDefault(),je(e.target.value)},placeholder:"* * * * *",value:pe},"cron_expression_input")]),(0,q.jsxs)(q.Fragment,{children:[(0,q.jsx)(y.Z,{mb:2,px:E.cd,children:(0,q.jsx)(m.Z,{children:"Settings"})}),(0,q.jsx)(h.Z,{light:!0,short:!0}),(0,q.jsx)(O.Z,{columnFlex:[null,1],rows:e})]})}),[pe,ke,ce,ue,Me]),Je=(0,u.useCallback)((function(e,n){U((function(t){return Object.entries(n).forEach((function(n){var r=(0,i.Z)(n,2),l=r[0],c=r[1];t[e][l]=c})),(0,X.Z)(t)}))}),[U]),Ge=(0,u.useMemo)((function(){return(0,q.jsxs)(q.Fragment,{children:[(0,q.jsx)(y.Z,{mb:E.cd,px:E.cd,children:(0,q.jsx)(m.Z,{children:"Settings"})}),(0,q.jsx)(h.Z,{light:!0,short:!0}),(0,q.jsx)(O.Z,{columnFlex:[null,1],rows:[[(0,q.jsxs)(f.Z,{alignItems:"center",children:[(0,q.jsx)(I.KJ,{default:!0,size:1.5*E.iI}),(0,q.jsx)(y.Z,{mr:1}),(0,q.jsx)(_.ZP,{default:!0,children:"Trigger name"})]},"trigger_name_event"),(0,q.jsx)(me.Z,{monospace:!0,onChange:function(e){e.preventDefault(),oe((function(n){return xe(xe({},n),{},{name:e.target.value})}))},placeholder:"Name this trigger",value:Oe},"trigger_name_input_event")]]}),(0,q.jsxs)(y.Z,{mb:2,mt:5,px:E.cd,children:[(0,q.jsx)(m.Z,{children:"Events"}),(0,q.jsxs)(_.ZP,{muted:!0,children:["Add 1 or more event that will trigger this pipeline to run.",(0,q.jsx)("br",{}),"If you add more than 1 event, this pipeline will trigger if any of the events are received."]}),(0,q.jsxs)(y.Z,{mt:E.Mq,children:[(0,q.jsx)(_.ZP,{bold:!0,large:!0,children:"AWS events"}),(0,q.jsxs)(_.ZP,{muted:!0,children:["In order to retrieve all the possible AWS events you can trigger your pipeline from,",(0,q.jsx)("br",{}),"you\u2019ll need to set 3 environment variables (",(0,q.jsx)(ee.Z,{href:"https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html",openNewWindow:!0,underline:!0,children:"more info here"}),"):"]}),(0,q.jsx)(y.Z,{mt:1,children:(0,q.jsxs)(he,{monospace:!0,ordered:!0,children:[(0,q.jsx)(_.ZP,{monospace:!0,children:"AWS_REGION_NAME"}),(0,q.jsx)(_.ZP,{monospace:!0,children:"AWS_ACCESS_KEY_ID"}),(0,q.jsx)(_.ZP,{monospace:!0,children:"AWS_SECRET_ACCESS_KEY"})]})})]})]}),(0,q.jsx)(h.Z,{light:!0,short:!0}),(null===M||void 0===M?void 0:M.length)>=1&&(0,q.jsx)(O.Z,{alignTop:!0,columnFlex:[1,1,2,null],columns:[{uuid:"Provider"},{uuid:"Event"},{uuid:"Pattern"},{label:function(){return""},uuid:"delete"}],rows:null===M||void 0===M?void 0:M.map((function(e,n){var t=e.event_type,r=e.name,i=e.pattern,l=e.id||"".concat(t,"-").concat(r,"-").concat(n,"-").concat(JSON.stringify(i)),c=[];return i&&JSON.stringify(i,null,2).split("\n").forEach((function(e){c.push("    ".concat(e))})),[(0,q.jsxs)(Z.Z,{monospace:!0,onChange:function(e){return Je(n,{event_type:e.target.value})},placeholder:"Event provider",value:t||"",children:[!t&&(0,q.jsx)("option",{value:""}),C.map((function(e){var n=e.label,t=e.uuid;return(0,q.jsx)("option",{value:t,children:n()},t)}))]},"event-provider-".concat(l)),(0,q.jsxs)(Z.Z,{monospace:!0,onChange:function(e){var t,r=e.target.value,i=null===(t=Re[r])||void 0===t?void 0:t.event_pattern;Je(n,{name:r,pattern:i?JSON.parse(i):null})},placeholder:"Event name",value:r,children:[!r&&(0,q.jsx)("option",{value:""}),Ue.map((function(e){var n=e.name;return(0,q.jsx)("option",{value:n,children:n},n)}))]},"event-name-".concat(l)),i&&(0,q.jsx)(K.Z,{language:"json",small:!0,source:c.join("\n")}),(0,q.jsx)(p.Z,{default:!0,iconOnly:!0,noBackground:!0,onClick:function(){return U((function(e){return(0,k.oM)(e,n)}))},children:(0,q.jsx)(I.rF,{default:!0,size:2*E.iI})},"remove_event")]}))}),(0,q.jsx)(y.Z,{p:E.cd,children:(0,q.jsx)(p.Z,{beforeIcon:(0,q.jsx)(I.mm,{size:2*E.iI}),onClick:function(){return U((function(e){return e.concat({})}))},outline:!0,children:"Add event matcher"})})]})}),[M,Ue,Oe]),Be=(0,u.useMemo)((function(){var e,n="".concat(window.origin,"/api/pipeline_schedules/").concat(null===r||void 0===r?void 0:r.id,"/pipeline_runs");return(e=window.location.port)&&(n=n.replace(e,"6789")),(0,q.jsxs)(q.Fragment,{children:[(0,q.jsx)(y.Z,{mb:E.cd,px:E.cd,children:(0,q.jsx)(m.Z,{children:"Settings"})}),(0,q.jsx)(h.Z,{light:!0,short:!0}),(0,q.jsx)(O.Z,{columnFlex:[null,1],rows:[[(0,q.jsxs)(f.Z,{alignItems:"center",children:[(0,q.jsx)(I.KJ,{default:!0,size:1.5*E.iI}),(0,q.jsx)(y.Z,{mr:1}),(0,q.jsx)(_.ZP,{default:!0,children:"Trigger name"})]},"trigger_name_api"),(0,q.jsx)(me.Z,{monospace:!0,onChange:function(e){e.preventDefault(),oe((function(n){return xe(xe({},n),{},{name:e.target.value})}))},placeholder:"Name this trigger",value:Oe},"trigger_name_input_api")]]}),(0,q.jsxs)(y.Z,{mb:2,mt:5,px:E.cd,children:[(0,q.jsx)(m.Z,{children:"Endpoint"}),(0,q.jsxs)(_.ZP,{muted:!0,children:["Make a ",(0,q.jsx)(_.ZP,{bold:!0,inline:!0,monospace:!0,children:"POST"})," request to the following endpoint:"]}),(0,q.jsx)(y.Z,{mt:E.Mq,children:(0,q.jsx)(Y.Z,{copiedText:n,linkText:n,monospace:!0,withCopyIcon:!0})})]}),(0,q.jsxs)(y.Z,{mb:2,mt:5,px:E.cd,children:[(0,q.jsx)(m.Z,{children:"Payload"}),(0,q.jsx)(_.ZP,{muted:!0,children:"You can optionally include runtime variables in your request payload. These runtime variables are accessible from within each pipeline block."}),(0,q.jsx)(y.Z,{mt:E.Mq,children:(0,q.jsx)(Y.Z,{withCopyIcon:!0,copiedText:'{\n  "pipeline_run": {\n    "variables": {\n      "key1": "value1",\n      "key2": "value2"\n    }\n  }\n}\n',children:(0,q.jsx)(K.Z,{language:"json",small:!0,source:'\n    {\n      "pipeline_run": {\n        "variables": {\n          "key1": "value1",\n          "key2": "value2"\n        }\n      }\n    }\n'})})})]}),(0,q.jsxs)(y.Z,{mb:2,mt:5,px:E.cd,children:[(0,q.jsx)(m.Z,{children:"Sample cURL command"}),(0,q.jsx)(y.Z,{mt:E.Mq,children:(0,q.jsx)(K.Z,{language:"bash",small:!0,source:"\n    curl -X POST ".concat(n,' \\\n      --header \'Content-Type: application/json\' \\\n      --data \'\n    {\n      "pipeline_run": {\n        "variables": {\n          "key1": "value1",\n          "key2": "value2"\n        }\n      }\n    }\'\n')})})]})]})}),[Oe,r,"object"]),Ke=!Pe||b.Xm.TIME===Pe&&!(j&&ke||!j&&ke&&_e)||b.Xm.EVENT===Pe&&(!(null!==M&&void 0!==M&&M.length)||!M.every((function(e){var n=e.event_type,t=e.name;return n&&t}))),Ye=(0,u.useMemo)((function(){return(0,q.jsxs)(y.Z,{p:E.cd,children:[!(0,R.Qr)(Ze)&&(0,q.jsxs)(q.Fragment,{children:[(0,q.jsxs)(f.Z,{alignItems:"center",children:[(0,q.jsx)(y.Z,{mr:2,children:(0,q.jsx)(ge.Z,{checked:z,onCheck:V})}),(0,q.jsx)(_.ZP,{monospace:!0,muted:!0,children:"Overwrite global variables"})]}),z&&re&&Object.entries(re).length>0&&(0,q.jsx)(y.Z,{mt:2,children:(0,q.jsx)(O.Z,{columnFlex:[null,1],columns:[{uuid:"Variable"},{uuid:"Value"}],rows:Object.entries(re).map((function(e){var n=(0,i.Z)(e,2),t=n[0],r=n[1];return[(0,q.jsx)(_.ZP,{default:!0,monospace:!0,children:t},"variable_".concat(t)),(0,q.jsx)(me.Z,{borderless:!0,monospace:!0,onChange:function(e){e.preventDefault(),ie((function(n){return xe(xe({},n),{},(0,c.Z)({},t,e.target.value))}))},paddingHorizontal:0,placeholder:"Variable value",value:r},"variable_uuid_input_".concat(t))]}))})})]}),(0,q.jsxs)(y.Z,{mt:2,children:[(0,q.jsxs)(f.Z,{alignItems:"center",children:[(0,q.jsx)(y.Z,{mr:2,children:(0,q.jsx)(ge.Z,{checked:W,onCheck:function(e){ne(e),e||oe((function(e){return xe(xe({},e),{},{slaAmount:0})}))}})}),(0,q.jsx)(_.ZP,{monospace:!0,muted:!0,children:"Configure trigger SLA"})]}),W&&(0,q.jsx)(y.Z,{mt:2,children:(0,q.jsx)(O.Z,{columnFlex:[null,1],rows:[[(0,q.jsxs)(f.Z,{alignItems:"center",children:[(0,q.jsx)(I.aw,{default:!0,size:1.5*E.iI}),(0,q.jsx)(y.Z,{mr:1}),(0,q.jsx)(_.ZP,{default:!0,children:"SLA"})]},"sla_detail"),(0,q.jsxs)(f.Z,{children:[(0,q.jsx)($.Z,{flex:1,children:(0,q.jsx)(me.Z,{fullWidth:!0,monospace:!0,noBorder:!0,onChange:function(e){e.preventDefault(),oe((function(n){return xe(xe({},n),{},{slaAmount:e.target.value})}))},placeholder:"Time",value:null===ce||void 0===ce?void 0:ce.slaAmount})}),(0,q.jsx)($.Z,{flex:1,children:(0,q.jsx)(Z.Z,{fullWidth:!0,monospace:!0,noBorder:!0,onChange:function(e){e.preventDefault(),oe((function(n){return xe(xe({},n),{},{slaUnit:e.target.value})}))},placeholder:"Select time unit",small:!0,value:null===ce||void 0===ce?void 0:ce.slaUnit,children:Object.keys(A.tL).map((function(e){return(0,q.jsx)("option",{value:e,children:"".concat(e,"(s)")},e)}))})})]},"sla_input_detail")]]})})]})]})}),[W,Ze,z,re,ce,ne,V]);return(0,q.jsxs)(q.Fragment,{children:[(0,q.jsxs)(v.Z,{after:Ye,breadcrumbs:[{label:function(){return"Triggers"},linkProps:{as:"/pipelines/".concat(s,"/triggers"),href:"/pipelines/[pipeline]/triggers"}},{label:function(){return null===r||void 0===r?void 0:r.name},linkProps:{as:"/pipelines/".concat(s,"/triggers/").concat(g),href:"/pipelines/[pipeline]/triggers/[...slug]"}}],pageName:T.M.TRIGGERS,pipeline:t,subheader:(0,q.jsxs)(f.Z,{alignItems:"center",children:[(0,q.jsx)(p.Z,{disabled:Ke,loading:qe,onClick:Le,outline:!0,primary:!0,children:"Save changes"}),(0,q.jsx)(y.Z,{mr:1}),(0,q.jsx)(p.Z,{linkProps:{href:"/pipelines/[pipeline]/triggers/[...slug]",as:"/pipelines/".concat(s,"/triggers/").concat(g)},noHoverUnderline:!0,outline:!0,sameColorAsText:!0,children:"Cancel"})]}),title:function(){return"Edit ".concat(null===r||void 0===r?void 0:r.name)},uuid:"triggers/edit",children:[(0,q.jsxs)(y.Z,{p:E.cd,children:[(0,q.jsxs)(y.Z,{mb:2,children:[(0,q.jsx)(m.Z,{children:"Trigger type"}),(0,q.jsx)(_.ZP,{muted:!0,children:"How would you like this pipeline to be triggered?"})]}),(0,q.jsx)(f.Z,{children:be(j).map((function(e){var n=e.label,t=e.description,r=e.uuid,i=Pe===r,l=Pe&&!i;return(0,q.jsx)(p.Z,{noBackground:!0,noBorder:!0,noPadding:!0,onClick:function(){b.Xm.EVENT!==r||null!==M&&void 0!==M&&M.length||U([{}]),oe((function(e){return xe(xe({},e),{},{schedule_type:r})}))},children:(0,q.jsx)(ve.U,{selected:i,children:(0,q.jsxs)(f.Z,{alignItems:"center",children:[(0,q.jsx)($.Z,{children:(0,q.jsx)("input",{checked:i,type:"radio"})}),(0,q.jsx)(y.Z,{mr:E.cd}),(0,q.jsxs)($.Z,{alignItems:"flex-start",flexDirection:"column",children:[(0,q.jsx)(m.Z,{bold:!0,default:!i&&!l,level:5,muted:!i&&l,children:n()}),(0,q.jsx)(_.ZP,{default:!i&&!l,leftAligned:!0,muted:l,children:t()})]})]})})},r)}))})]}),(0,q.jsxs)(y.Z,{mt:5,children:[b.Xm.TIME===Pe&&Xe,b.Xm.EVENT===Pe&&Ge,b.Xm.API===Pe&&Be]})]}),S&&(0,q.jsx)(Q.Z,xe(xe({},S),{},{onClose:function(){return w(null)}}))]})},ye=t(70543);function Oe(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function _e(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?Oe(Object(t),!0).forEach((function(n){(0,c.Z)(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):Oe(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function Pe(e){var n=e.pipelineScheduleId,t=e.pipelineUUID,r=e.subpath,i=P.ZP.variables.pipelines.list(t).data,l=null===i||void 0===i?void 0:i.variables,c=P.ZP.pipeline_schedules.detail(n,{include_event_matchers:!0}),o=c.data,s=c.mutate,u=null===o||void 0===o?void 0:o.pipeline_schedule,a=P.ZP.pipelines.detail(t).data,d=_e(_e({},null===a||void 0===a?void 0:a.pipeline),{},{uuid:t});return ye.b===r?(0,q.jsx)(Ze,{fetchPipelineSchedule:s,pipeline:d,pipelineSchedule:u,variables:l}):(0,q.jsx)(W,{fetchPipelineSchedule:s,pipeline:d,pipelineSchedule:u,variables:l})}Pe.getInitialProps=function(){var e=(0,l.Z)(s().mark((function e(n){var t,r,l,c,o,u;return s().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(t=n.query,r=t.pipeline,l=t.slug,!Array.isArray(l)){e.next=4;break}return c=(0,i.Z)(l,2),o=c[0],u=c[1],e.abrupt("return",{pipelineScheduleId:o,pipelineUUID:r,subpath:u});case 4:return e.abrupt("return",{pipelineUUID:r});case 5:case"end":return e.stop()}}),e)})));return function(n){return e.apply(this,arguments)}}();var Se=Pe},95488:function(e,n,t){(window.__NEXT_P=window.__NEXT_P||[]).push(["/pipelines/[pipeline]/triggers/[...slug]",function(){return t(54183)}])}},function(e){e.O(0,[4259,2212,7689,6674,4804,5872,1774,2524,4495,1374,5763,6792,1273,8965,9898,2151,5703,4846,7788,9774,2888,179],(function(){return n=95488,e(e.s=n);var n}));var n=e.O();_N_E=n}]);