(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[1221],{66757:function(n,e,t){"use strict";var r=t(19319),i=t(94178),o=t(67240),c="localStorage"in t.g&&t.g.localStorage?t.g.localStorage:r;function u(n,e){return 1===arguments.length?l(n):a(n,e)}function l(n){const e=c.getItem(n);return i(e)}function a(n,e){try{return c.setItem(n,JSON.stringify(e)),!0}catch(t){return!1}}u.set=a,u.get=l,u.remove=function(n){return c.removeItem(n)},u.clear=function(){return c.clear()},u.backend=function(n){return n&&(c=n),c},u.on=o.on,u.off=o.off,n.exports=u},94178:function(n){"use strict";n.exports=function(n){const e=function(n){try{return JSON.parse(n)}catch(e){return n}}(n);return void 0===e?null:e}},19319:function(n){"use strict";var e={};n.exports={getItem:function(n){return n in e?e[n]:null},setItem:function(n,t){return e[n]=t,!0},removeItem:function(n){return!!(n in e)&&delete e[n]},clear:function(){return e={},!0}}},67240:function(n,e,t){"use strict";var r=t(94178),i={};function o(n){n||(n=t.g.event);var e=i[n.key];e&&e.forEach((function(e){e(r(n.newValue),r(n.oldValue),n.url||n.uri)}))}n.exports={on:function(n,e){i[n]?i[n].push(e):i[n]=[e],t.g.addEventListener?t.g.addEventListener("storage",o,!1):t.g.attachEvent?t.g.attachEvent("onstorage",o):t.g.onstorage=o},off:function(n,e){var t=i[n];t.length>1?t.splice(t.indexOf(e),1):i[n]=[]}}},72454:function(n,e,t){"use strict";t.d(e,{E7:function(){return h},HS:function(){return p},Nk:function(){return d},k1:function(){return s},lm:function(){return f}});var r=t(9518),i=t(23831),o=t(73942),c=t(3055),u=t(49125),l=t(37391),a=t(90880),s=u.cd*u.iI+5*u.iI+u.cd*u.iI,d=r.default.div.withConfig({displayName:"indexstyle__ContainerStyle",componentId:"sc-ecogjt-0"})(["display:flex;flex-direction:row;height:calc(100vh - ","px);position:fixed;top:","px;width:100%;",""],c.Mz,c.Mz,(function(n){return"\n    background-color: ".concat((n.theme.background||i.Z.background).page,";\n  ")})),f=r.default.div.withConfig({displayName:"indexstyle__VerticalNavigationStyle",componentId:"sc-ecogjt-1"})(["padding:","px;",""],u.cd*u.iI,(function(n){return"\n    background-color: ".concat((n.theme.background||i.Z.background).panel,";\n    border-right: 1px solid ").concat((n.theme.borders||i.Z.borders).medium,";\n  ")})),p=r.default.div.withConfig({displayName:"indexstyle__SubheaderStyle",componentId:"sc-ecogjt-2"})(["width:fit-content;padding:","px;position:relative;z-index:2;",""],u.cd*u.iI,(function(n){return"\n    border-bottom: 1px solid ".concat((n.theme.borders||i.Z.borders).medium,";\n  ")})),h=(r.default.div.withConfig({displayName:"indexstyle__ContentStyle",componentId:"sc-ecogjt-3"})([""," overflow:auto;",""],l.w5,(function(n){return"\n    height: calc(100vh - ".concat(c.Mz+(n.heightOffset||0),"px);\n  ")})),r.default.div.withConfig({displayName:"indexstyle__NavigationItemStyle",componentId:"sc-ecogjt-4"})(["display:flex;align-items:center;justify-content:center;padding:","px;border-radius:","px;",""],u.iI,o.n_,(function(n){return n.primary&&"\n    ".concat((0,a.eR)(),"\n    background: ").concat((n.theme||i.Z).chart.backgroundPrimary,";\n    border: 1px solid ").concat((n.theme||i.Z).feature.active,";\n\n    &:hover {\n      background-color: ").concat((n.theme||i.Z).interactive.linkSecondary,";\n    }\n  ")})))},51404:function(n,e,t){"use strict";t.d(e,{Z:function(){return P}});var r=t(77555),i=t(82684),o=t(93461),c=t(57384),u=t(80845),l=t(72454),a=t(28598);function s(n,e){var t=n.children;return(0,a.jsx)(l.HS,{ref:e,children:t})}var d=i.forwardRef(s),f=t(32063),p=t(34376),h=t(61519),g=t(57639),v=t(882),m=t(31866);var b=function(n){var e=n.size;return(0,a.jsxs)("svg",{width:e,height:e,viewBox:"0 0 26 26",fill:"none",xmlns:"http://www.w3.org/2000/svg",children:[(0,a.jsx)("path",{"fill-rule":"evenodd","clip-rule":"evenodd",d:"M9.86364 2.5H4.13636C3.68449 2.5 3.31818 2.94772 3.31818 3.5V7.5C3.31818 8.05228 3.68449 8.5 4.13636 8.5H9.86364C10.3155 8.5 10.6818 8.05228 10.6818 7.5V3.5C10.6818 2.94772 10.3155 2.5 9.86364 2.5ZM4.13636 1.5C3.23263 1.5 2.5 2.39543 2.5 3.5V7.5C2.5 8.60457 3.23263 9.5 4.13636 9.5H5.5V16.1667V16.5H4.13636C3.23263 16.5 2.5 17.3954 2.5 18.5V22.5C2.5 23.6046 3.23263 24.5 4.13636 24.5H9.86364C10.7674 24.5 11.5 23.6046 11.5 22.5V18.5C11.5 17.3954 10.7674 16.5 9.86364 16.5H6.5V16.1667C6.5 14.9394 7.61929 13.9444 9 13.9444H16C17.933 13.9444 19.5 12.5516 19.5 10.8333V9.5H21.8636C22.7674 9.5 23.5 8.60457 23.5 7.5V3.5C23.5 2.39543 22.7674 1.5 21.8636 1.5H16.1364C15.2326 1.5 14.5 2.39543 14.5 3.5V7.5C14.5 8.60457 15.2326 9.5 16.1364 9.5H18.5V10.8333C18.5 12.0606 17.3807 13.0556 16 13.0556H9C8.02066 13.0556 7.13526 13.4131 6.5 13.9893V9.5H9.86364C10.7674 9.5 11.5 8.60457 11.5 7.5V3.5C11.5 2.39543 10.7674 1.5 9.86364 1.5H4.13636ZM9.86364 17.5H6.5H5.5H4.13636C3.68449 17.5 3.31818 17.9477 3.31818 18.5V22.5C3.31818 23.0523 3.68449 23.5 4.13636 23.5H9.86364C10.3155 23.5 10.6818 23.0523 10.6818 22.5V18.5C10.6818 17.9477 10.3155 17.5 9.86364 17.5ZM16.1364 2.5H21.8636C22.3155 2.5 22.6818 2.94772 22.6818 3.5V7.5C22.6818 8.05228 22.3155 8.5 21.8636 8.5H16.1364C15.6845 8.5 15.3182 8.05228 15.3182 7.5V3.5C15.3182 2.94772 15.6845 2.5 16.1364 2.5Z",fill:"url(#paint0_linear_2738_141228)"}),(0,a.jsx)("defs",{children:(0,a.jsxs)("linearGradient",{id:"paint0_linear_2738_141228",x1:"2.5",y1:"13",x2:"23.5",y2:"13",gradientUnits:"userSpaceOnUse",children:[(0,a.jsx)("stop",{offset:"0.28125",stopColor:"#7D55EC"}),(0,a.jsx)("stop",{offset:"1",stopColor:"#2AB2FE"})]})})]})},y=t(86673),x=t(19711),w=t(46261),C=t(10503),j=t(99994),O=t(49125),A=3*O.iI;var k=function(n){var e=n.navigationItems,t=(0,p.useRouter)().pathname,r=(0,i.useMemo)((function(){return(e||[{Icon:C.rV,IconSelected:b,id:"pipelines",label:function(){return"Pipelines"},linkProps:{href:"pipelines"}},{Icon:C.pd,IconSelected:h.Z,id:"pipeline-runs",label:function(){return"Pipelines runs"},linkProps:{href:"pipeline-runs"}}]).map((function(n,e){var r=n.Icon,i=n.IconSelected,o=n.id,c=n.isSelected,u=n.label,s=n.linkProps,d=c?c(t):!!t.match(new RegExp("^/".concat(o,"[/]*"))),f=d&&i?i:r;return(0,a.jsx)(y.Z,{mt:e>=1?O.cd:0,children:(0,a.jsxs)(w.Z,{height:5*O.iI,label:u(),size:null,widthFitContent:!0,children:[d&&i&&(0,a.jsx)(v.Z,{backgroundGradient:j.yr,backgroundPanel:!0,basic:!0,borderWidth:2,linkProps:s,paddingUnits:1,children:(0,a.jsx)("div",{style:{height:A,width:A},children:(0,a.jsx)(f,{muted:!0,size:A})})}),!d&&(0,a.jsx)(m.ZP,{block:!0,noHoverUnderline:!0,noPadding:!0,linkProps:s,sameColorAsText:!0,uuid:"VerticalNavigation/".concat(o),children:(0,a.jsx)(l.E7,{primary:!f,children:f?(0,a.jsx)(f,{muted:!0,size:A}):(0,a.jsx)(x.ZP,{children:"Edit"})})})]})},"button-".concat(o))}))}),[e,t]);return(0,a.jsx)(g.Z,{children:r})},E=t(41374),Z=t(3055),R=t(91427),_=t(24141);var P=function(n){var e,t=n.after,s=n.afterHidden,p=n.afterWidth,h=n.before,g=n.beforeWidth,v=n.breadcrumbs,m=n.children,b=n.headerMenuItems,y=n.navigationItems,x=n.subheaderChildren,w=n.title,C=n.uuid,j=(0,_.i)().width,O="dashboard_after_width_".concat(C),A="dashboard_before_width_".concat(C),P=(0,i.useRef)(null),T=(0,i.useState)((0,R.U2)(O,p)),S=T[0],H=T[1],D=(0,i.useState)(!1),I=D[0],N=D[1],V=(0,i.useState)((0,R.U2)(A,g)),M=V[0],z=V[1],B=(0,i.useState)(!1),L=B[0],F=B[1],Y=(0,i.useState)(null),U=(Y[0],Y[1]),W=E.ZP.projects.list().data,X=null===W||void 0===W?void 0:W.projects,q=[];return v?q.push.apply(q,(0,r.Z)(v)):(null===X||void 0===X?void 0:X.length)>=1&&q.push.apply(q,[{label:function(){var n;return null===(n=X[0])||void 0===n?void 0:n.name}},{bold:!0,label:function(){return w}}]),(0,i.useEffect)((function(){null===P||void 0===P||!P.current||I||L||null===U||void 0===U||U(P.current.getBoundingClientRect().width)}),[I,S,L,M,null===P||void 0===P?void 0:P.current,U,j]),(0,i.useEffect)((function(){I||(0,R.t8)(O,S)}),[s,I,S]),(0,i.useEffect)((function(){L||(0,R.t8)(A,M)}),[L,M]),(0,a.jsxs)(a.Fragment,{children:[(0,a.jsx)(c.Z,{title:w}),(0,a.jsx)(u.Z,{breadcrumbs:q,menuItems:b,project:null===X||void 0===X?void 0:X[0],version:null===X||void 0===X||null===(e=X[0])||void 0===e?void 0:e.version}),(0,a.jsxs)(l.Nk,{children:[0!==(null===y||void 0===y?void 0:y.length)&&(0,a.jsx)(l.lm,{children:(0,a.jsx)(k,{navigationItems:y})}),(0,a.jsx)(o.Z,{flex:1,flexDirection:"column",children:(0,a.jsxs)(f.Z,{after:t,afterHeightOffset:Z.Mz,afterHidden:s,afterMousedownActive:I,afterWidth:S,before:h,beforeHeightOffset:Z.Mz,beforeMousedownActive:L,beforeWidth:l.k1+(h?M:0),hideAfterCompletely:!0,leftOffset:h?l.k1:null,mainContainerRef:P,setAfterMousedownActive:N,setAfterWidth:H,setBeforeMousedownActive:F,setBeforeWidth:z,children:[x&&(0,a.jsx)(d,{children:x}),m]})})]})]})}},17903:function(n,e,t){"use strict";t.d(e,{Z:function(){return j}});var r=t(82394),i=t(12691),o=t.n(i),c=t(82684),u=t(67971),l=t(10919),a=t(86673),s=t(19711),d=t(46261),f=t(9518),p=t(23831),h=t(49125),g=f.default.table.withConfig({displayName:"indexstyle__TableStyle",componentId:"sc-1wzfyed-0"})(["contain:size;width:100%;",""],(function(n){return n.columnBorders&&"\n    border-collapse: separate;\n  "})),v=f.default.tr.withConfig({displayName:"indexstyle__TableRowStyle",componentId:"sc-1wzfyed-1"})(["",""],(function(n){return!n.noHover&&"\n    &:hover {\n      background: ".concat((n.theme.interactive||p.Z.interactive).rowHoverBackground,";\n      cursor: pointer;\n    }\n  ")})),m=(0,f.css)(["text-overflow:ellipsis;white-space:nowrap;"," "," "," "," "," ",""],(function(n){return!n.alignTop&&"\n    vertical-align: middle;\n  "}),(function(n){return n.alignTop&&"\n    vertical-align: top;\n  "}),(function(n){return!n.noBorder&&"\n    border-bottom: 1px solid ".concat((n.theme.borders||p.Z.borders).light,";\n  ")}),(function(n){return n.compact&&"\n    padding: ".concat(h.iI/2,"px ").concat(h.iI,"px;\n  ")}),(function(n){return!n.compact&&"\n    padding: ".concat(h.iI,"px ").concat(2*h.iI,"px;\n  ")}),(function(n){return n.maxWidth&&"\n    max-width: ".concat(n.maxWidth,";\n  ")})),b=f.default.th.withConfig({displayName:"indexstyle__TableHeadStyle",componentId:"sc-1wzfyed-2"})([""," "," "," ",""],m,(function(n){return n.columnBorders&&"\n    border: 1px solid ".concat((n.theme.borders||p.Z.borders).light,";\n    border-right: none;\n  ")}),(function(n){return n.columnBorders&&n.last&&"\n    border-right: 1px solid ".concat((n.theme.borders||p.Z.borders).light,";\n  ")}),(function(n){return n.sticky&&"\n    background-color: ".concat((n.theme||p.Z).background.panel,";\n    z-index: 1;\n    position: sticky;\n    top: 0;\n\n    &:first-child {\n      left: 0;\n      z-index: 2;\n    }\n  ")})),y=f.default.td.withConfig({displayName:"indexstyle__TableDataStyle",componentId:"sc-1wzfyed-3"})([""," "," "," "," "," ",""],m,(function(n){return n.columnBorders&&"\n    border-left: 1px solid ".concat((n.theme.borders||p.Z.borders).light,";\n  ")}),(function(n){return n.columnBorders&&n.last&&"\n    border-right: 1px solid ".concat((n.theme.borders||p.Z.borders).light,";\n  ")}),(function(n){return n.stickyFirstColumn&&"\n    background-color: ".concat((n.theme||p.Z).background.panel,";\n    z-index: 1;\n    position: sticky;\n    left: 0;\n  ")}),(function(n){return n.selected&&"\n    background-color: ".concat((n.theme.interactive||p.Z.interactive).activeBorder,";\n  ")}),(function(n){return n.wrapColumns&&"\n    white-space: break-spaces;\n  "})),x=t(28598);function w(n,e){var t=Object.keys(n);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(n);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(n,e).enumerable}))),t.push.apply(t,r)}return t}function C(n){for(var e=1;e<arguments.length;e++){var t=null!=arguments[e]?arguments[e]:{};e%2?w(Object(t),!0).forEach((function(e){(0,r.Z)(n,e,t[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(n,Object.getOwnPropertyDescriptors(t)):w(Object(t)).forEach((function(e){Object.defineProperty(n,e,Object.getOwnPropertyDescriptor(t,e))}))}return n}var j=function(n){var e=n.alignTop,t=n.buildLinkProps,r=n.columnBorders,i=n.columnFlex,f=n.columnMaxWidth,p=n.columns,h=void 0===p?[]:p,m=n.compact,w=n.isSelectedRow,j=n.noBorder,O=n.noHeader,A=n.onClickRow,k=n.rows,E=n.stickyFirstColumn,Z=n.stickyHeader,R=n.uuid,_=n.wrapColumns,P=(0,c.useMemo)((function(){return i.reduce((function(n,e){return n+(e||0)}),0)}),i),T=(0,c.useCallback)((function(n){if(i[n]){var e=Math.round(i[n]/P*100);return"".concat(e,"%")}return null}),[]),S=(0,c.useMemo)((function(){return null===k||void 0===k?void 0:k.map((function(n,i){var c=null===t||void 0===t?void 0:t(i),u=n.map((function(t,o){return(0,x.jsx)(y,{alignTop:e,columnBorders:r,compact:m,last:o===n.length-1,maxWidth:null===f||void 0===f?void 0:f(o),noBorder:j,selected:null===w||void 0===w?void 0:w(i),stickyFirstColumn:E&&0===o,width:T(o),wrapColumns:_,children:t},"".concat(R,"-row-").concat(i,"-cell-").concat(o))})),a=(0,x.jsx)(v,{noHover:!(c||A),onClick:A?function(){return A(i)}:null,children:u},"".concat(R,"-row-").concat(i));return c?(0,x.jsx)(o(),C(C({},c),{},{passHref:!0,children:(0,x.jsx)(l.Z,{fullWidth:!0,noHoverUnderline:!0,noOutline:!0,style:{display:"table-row-group"},verticalAlignContent:!0,children:a})})):a}))}),[e,t,T,f,h,m,w,j,A,k]);return(0,x.jsxs)(g,{columnBorders:r,children:[(null===h||void 0===h?void 0:h.length)>=1&&!O&&(0,x.jsx)(v,{noHover:!0,children:h.map((function(n,e){return(0,x.jsx)(b,{columnBorders:r,compact:m,last:e===h.length-1,noBorder:j,sticky:Z,children:(0,x.jsxs)(u.Z,{alignItems:"center",children:[(0,x.jsx)(s.ZP,{bold:!0,leftAligned:!0,monospace:!0,muted:!0,children:n.label?n.label():n.uuid}),n.tooltipMessage&&(0,x.jsx)(a.Z,{ml:"4px",children:(0,x.jsx)(d.Z,{appearBefore:!0,label:(0,x.jsx)(s.ZP,{leftAligned:!0,children:n.tooltipMessage}),lightBackground:!0,primary:!0})})]})},"".concat(R,"-col-").concat(n.uuid,"-").concat(e))}))}),S]})}},86422:function(n,e,t){"use strict";t.d(e,{$W:function(){return d},DA:function(){return s},HX:function(){return h},J8:function(){return p},Qj:function(){return g},Ut:function(){return y},V4:function(){return b},VZ:function(){return f},dO:function(){return a},f2:function(){return m},iZ:function(){return v},t6:function(){return c},tf:function(){return l}});var r,i,o,c,u=t(82394);!function(n){n.PYTHON="python",n.R="r",n.SQL="sql",n.YAML="yaml"}(c||(c={}));var l,a=(r={},(0,u.Z)(r,c.PYTHON,"PY"),(0,u.Z)(r,c.R,"R"),(0,u.Z)(r,c.SQL,"SQL"),(0,u.Z)(r,c.YAML,"YAML"),r);!function(n){n.CHART="chart",n.DATA_EXPORTER="data_exporter",n.DATA_LOADER="data_loader",n.DBT="dbt",n.SCRATCHPAD="scratchpad",n.SENSOR="sensor",n.TRANSFORMER="transformer"}(l||(l={}));var s,d=[l.CHART,l.DATA_EXPORTER,l.DATA_LOADER,l.SCRATCHPAD,l.SENSOR,l.TRANSFORMER],f=[l.DATA_EXPORTER,l.DATA_LOADER],p=[l.DATA_EXPORTER,l.DATA_LOADER,l.TRANSFORMER],h=[l.DATA_EXPORTER,l.DATA_LOADER,l.DBT,l.TRANSFORMER],g=[l.CHART,l.SCRATCHPAD,l.SENSOR],v=[l.SCRATCHPAD];!function(n){n.EXECUTED="executed",n.FAILED="failed",n.NOT_EXECUTED="not_executed",n.UPDATED="updated"}(s||(s={}));var m=[l.DATA_EXPORTER,l.TRANSFORMER],b=(i={},(0,u.Z)(i,l.DATA_EXPORTER,"Data exporter"),(0,u.Z)(i,l.DATA_LOADER,"Data loader"),(0,u.Z)(i,l.SCRATCHPAD,"Scratchpad"),(0,u.Z)(i,l.SENSOR,"Sensor"),(0,u.Z)(i,l.TRANSFORMER,"Transformer"),i),y=[l.DATA_LOADER,l.TRANSFORMER,l.DATA_EXPORTER];o={},(0,u.Z)(o,l.DATA_EXPORTER,"DE"),(0,u.Z)(o,l.DATA_LOADER,"DL"),(0,u.Z)(o,l.SCRATCHPAD,"SP"),(0,u.Z)(o,l.SENSOR,"SR"),(0,u.Z)(o,l.TRANSFORMER,"TF")},93348:function(n,e,t){"use strict";t.d(e,{U5:function(){return u},Xm:function(){return i},Z4:function(){return l},fq:function(){return c}});var r,i,o=t(82394);!function(n){n.API="api",n.EVENT="event",n.TIME="time"}(i||(i={}));var c,u,l=(r={},(0,o.Z)(r,i.API,(function(){return"API"})),(0,o.Z)(r,i.EVENT,(function(){return"event"})),(0,o.Z)(r,i.TIME,(function(){return"schedule"})),r);!function(n){n.ACTIVE="active",n.INACTIVE="inactive"}(c||(c={})),function(n){n.ONCE="@once",n.HOURLY="@hourly",n.DAILY="@daily",n.WEEKLY="@weekly",n.MONTHLY="@monthly"}(u||(u={}))},98781:function(n,e,t){"use strict";t.d(e,{a:function(){return c},q:function(){return i}});var r,i,o=t(82394);!function(n){n.INTEGRATION="integration",n.PYTHON="python",n.PYSPARK="pyspark",n.STREAMING="streaming"}(i||(i={}));var c=(r={},(0,o.Z)(r,i.PYTHON,"python3"),(0,o.Z)(r,i.PYSPARK,"pysparkkernel"),r)},30264:function(n,e,t){"use strict";var r=t(82394),i=t(26304),o=(t(82684),t(47999)),c=t(62084),u=t(28598),l=["children","items","open","onClickCallback","onClickOutside","parentRef","uuid"];function a(n,e){var t=Object.keys(n);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(n);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(n,e).enumerable}))),t.push.apply(t,r)}return t}function s(n){for(var e=1;e<arguments.length;e++){var t=null!=arguments[e]?arguments[e]:{};e%2?a(Object(t),!0).forEach((function(e){(0,r.Z)(n,e,t[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(n,Object.getOwnPropertyDescriptors(t)):a(Object(t)).forEach((function(e){Object.defineProperty(n,e,Object.getOwnPropertyDescriptor(t,e))}))}return n}e.Z=function(n){var e=n.children,t=n.items,r=n.open,a=n.onClickCallback,d=n.onClickOutside,f=n.parentRef,p=n.uuid,h=(0,i.Z)(n,l),g=(0,u.jsxs)("div",{style:{position:"relative",zIndex:d?3:2},children:[(0,u.jsx)("div",{ref:f,children:e}),(0,u.jsx)(c.Z,s(s({},h),{},{items:t,onClickCallback:a,open:r,parentRef:f,uuid:p}))]});return d?(0,u.jsx)(o.Z,{onClickOutside:d,open:!0,children:g}):g}},61519:function(n,e,t){"use strict";var r=t(28598);e.Z=function(n){var e=n.size;return(0,r.jsxs)("svg",{width:e,height:e,viewBox:"0 0 26 26",fill:"none",xmlns:"http://www.w3.org/2000/svg",children:[(0,r.jsx)("path",{fillRule:"evenodd",clipRule:"evenodd",d:"M3 3H9V9H3V3ZM10 2V9H17V16H24V24H17H16H10H9H2V17V16V10V9V2H10ZM16 23V17H10V23H16ZM17 23H23V17H17V23ZM16 16V10H10V16H16ZM9 10V16H3V10H9ZM9 17V23H3V17H9Z",fill:"url(#paint0_linear_2738_140355)"}),(0,r.jsx)("defs",{children:(0,r.jsxs)("linearGradient",{id:"paint0_linear_2738_140355",x1:"2",y1:"13",x2:"24",y2:"13",gradientUnits:"userSpaceOnUse",children:[(0,r.jsx)("stop",{offset:"0.28125",stopColor:"#7D55EC"}),(0,r.jsx)("stop",{offset:"1",stopColor:"#2AB2FE"})]})})]})}},5545:function(n,e,t){"use strict";t.r(e);var r=t(82394),i=t(12757),o=t(83455),c=t(82684),u=t(34376),l=t(60328),a=t(51404),s=t(93461),d=t(30264),f=t(31866),p=t(98781),h=t(17903),g=t(19711),v=t(41374),m=t(10503),b=t(86422),y=t(99994),x=t(93348),w=t(49125),C=t(5679),j=t(96510),O=t(66653),A=t(28598);function k(n,e){var t=Object.keys(n);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(n);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(n,e).enumerable}))),t.push.apply(t,r)}return t}function E(n){for(var e=1;e<arguments.length;e++){var t=null!=arguments[e]?arguments[e]:{};e%2?k(Object(t),!0).forEach((function(e){(0,r.Z)(n,e,t[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(n,Object.getOwnPropertyDescriptors(t)):k(Object(t)).forEach((function(e){Object.defineProperty(n,e,Object.getOwnPropertyDescriptor(t,e))}))}return n}e.default=function(){var n=(0,u.useRouter)(),e=(0,c.useState)({}),t=e[0],k=e[1],Z=(0,c.useState)(!1),R=Z[0],_=Z[1],P=(0,c.useRef)(null),T=v.ZP.pipelines.list({include_schedules:1}),S=T.data,H=T.mutate,D=(0,c.useMemo)((function(){return(null===S||void 0===S?void 0:S.pipelines)||[]}),[S]),I=(0,c.useCallback)((function(){return _(!1)}),[]),N=(0,o.Db)(v.ZP.pipelines.useCreate(),{onSuccess:function(e){return(0,j.wD)(e,{callback:function(e){var t=e.pipeline.uuid;n.push("/pipelines/[pipeline]/edit","/pipelines/".concat(t,"/edit"))},onErrorCallback:function(n){var e=n.error,t=e.errors,r=e.message;console.log(t,r)}})}}),V=(0,i.Z)(N,2),M=V[0],z=V[1].isLoading,B=(0,o.Db)((function(n){return v.ZP.pipelines.useUpdate(n.uuid)({pipeline:n})}),{onSuccess:function(n){return(0,j.wD)(n,{callback:function(n){var e=n.pipeline.uuid;k((function(n){return E(E({},n),{},(0,r.Z)({},e,!1))})),H()},onErrorCallback:function(n){var e=n.error,t=e.errors,r=e.message;console.log(t,r)}})}}),L=(0,i.Z)(B,1)[0];return(0,A.jsx)(a.Z,{subheaderChildren:(0,A.jsx)(d.Z,{disableKeyboardShortcuts:!0,items:[{label:function(){return"Standard (batch)"},onClick:function(){return M({pipeline:{name:(0,C.Y6)()}})},uuid:"Pipelines/NewPipelineMenu/standard"},{label:function(){return"Data integration"},onClick:function(){return M({pipeline:{name:(0,C.Y6)(),type:p.q.INTEGRATION}})},uuid:"Pipelines/NewPipelineMenu/integration"},{label:function(){return"Streaming"},onClick:function(){return M({pipeline:{name:(0,C.Y6)(),type:p.q.STREAMING}})},uuid:"Pipelines/NewPipelineMenu/streaming"}],onClickCallback:I,onClickOutside:I,open:R,parentRef:P,roundedStyle:!0,uuid:"pipelines/new_pipeline_menu",children:(0,A.jsx)(f.ZP,{background:y.eW,beforeElement:(0,A.jsx)(m.mm,{size:2.5*w.iI}),bold:!0,inline:!0,loading:z,onClick:function(n){n.preventDefault(),_((function(n){return!n}))},uuid:"pipelines/new_pipeline_button",children:"New pipeline"})}),title:"Pipelines",uuid:"pipelines/index",children:(0,A.jsx)(h.Z,{buildLinkProps:function(n){return{as:"/pipelines/".concat(D[n].uuid),href:"/pipelines/[pipeline]"}},columnFlex:[null,1,7,1,1,1,null],columns:[{label:function(){return""},uuid:"action"},{uuid:"Status"},{uuid:"Name"},{uuid:"Type"},{uuid:"Blocks"},{uuid:"Triggers"},{label:function(){return""},uuid:"view"}],rows:D.map((function(n,e){var i=n.blocks,o=(n.name,n.schedules),c=n.type,u=n.uuid,a=i.filter((function(n){var e=n.type;return b.tf.SCRATCHPAD!==e})).length,d=o.length,f=o.find((function(n){var e=n.status;return x.fq.ACTIVE===e}));return[d>=1?(0,A.jsx)(l.Z,{iconOnly:!0,loading:!!t[u],noBackground:!0,noBorder:!0,noPadding:!0,onClick:function(e){(0,O.j)(e),k((function(n){return E(E({},n),{},(0,r.Z)({},u,!0))})),L(E(E({},n),{},{status:f?x.fq.INACTIVE:x.fq.ACTIVE}))},children:f?(0,A.jsx)(m.dz,{muted:!0,size:2*w.iI}):(0,A.jsx)(m.Py,{default:!0,size:2*w.iI})}):null,(0,A.jsx)(g.ZP,{default:!f,monospace:!0,success:!!f,children:f?x.fq.ACTIVE:d>=1?x.fq.INACTIVE:"no schedules"},"pipeline_status_".concat(e)),(0,A.jsx)(g.ZP,{children:u},"pipeline_name_".concat(e)),(0,A.jsx)(g.ZP,{children:c===p.q.PYTHON?"Standard":(0,C.kC)(c)},"pipeline_type_".concat(e)),(0,A.jsx)(g.ZP,{default:0===a,monospace:!0,children:a},"pipeline_block_count_".concat(e)),(0,A.jsx)(g.ZP,{default:0===d,monospace:!0,children:d},"pipeline_trigger_count_".concat(e)),(0,A.jsx)(s.Z,{flex:1,justifyContent:"flex-end",children:(0,A.jsx)(m._Q,{default:!0,size:2*w.iI})},"chevron_icon_".concat(e))]}))})})}},5679:function(n,e,t){"use strict";t.d(e,{RA:function(){return f},kC:function(){return p},vg:function(){return x},T3:function(){return O},Mp:function(){return h},Pb:function(){return a},HW:function(){return C},HD:function(){return s},wX:function(){return g},x6:function(){return v},_6:function(){return m},zf:function(){return w},Y6:function(){return k},Lo:function(){return E},Tz:function(){return j},We:function(){return d},QV:function(){return A},C5:function(){return y}});var r=t(12757),i=["aged","ancient","autumn","billowing","bitter","black","blue","bold","broken","cold","cool","crimson","damp","dark","dawn","delicate","divine","dry","empty","falling","floral","fragrant","frosty","green","hidden","holy","icy","late","lingering","little","lively","long","misty","morning","muddy","nameless","old","patient","polished","proud","purple","quiet","red","restless","rough","shy","silent","small","snowy","solitary","sparkling","spring","still","summer","throbbing","twilight","wandering","weathered","white","wild","winter","wispy","withered","young"],o=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],c=(t(92083),["bird","breeze","brook","bush","butterfly","cherry","cloud","darkness","dawn","dew","dream","dust","feather","field","fire","firefly","flower","fog","forest","frog","frost","glade","glitter","grass","haze","hill","lake","leaf","meadow","moon","morning","mountain","night","paper","pine","pond","rain","resonance","river","sea","shadow","shape","silence","sky","smoke","snow","snowflake","sound","star","sun","sun","sunset","surf","thunder","tree","violet","voice","water","water","waterfall","wave","wildflower","wind","wood"]),u=["0","1","2","3","4","5","6","7","8","9"],l=t(24224);function a(n){try{JSON.parse(n)}catch(e){return!1}return!0}function s(n){return"string"===typeof n}function d(n){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"_";return n.split(" ").join(e)}function f(n){return n.split(" ").join("_")}function p(n){return n?n.charAt(0).toUpperCase()+n.slice(1):""}function h(){var n=arguments.length>0&&void 0!==arguments[0]?arguments[0]:1;return String((new Date).getTime()*n)}function g(n){return n.charAt(0).toLowerCase()+n.slice(1)}function v(n){if(null===n||"undefined"===typeof n)return"";var e=n.toString().split("."),t=(0,r.Z)(e,2),i=t[0],o=t[1],c=i.toString().replace(/\B(?=(\d{3})+(?!\d))/g,",");return o?"".concat(c,".").concat(o):c}function m(n,e){var t,r=arguments.length>2&&void 0!==arguments[2]&&arguments[2],i=e,o=void 0!==i&&null!==i;if(o||(i=2),1===i)t=n;else{var c=n.length,u=n[c-1];t="y"===u&&"day"!==n?"".concat(n.slice(0,c-1),"ies"):"".concat(n,"s"===u?"es":"s")}if(o){var l=r?v(i):i;return"".concat(l," ").concat(t)}return t}function b(n){return null===n||void 0===n?void 0:n.replace(/_/g," ")}function y(n){var e=n.length;return"ies"===n.slice(e-3,e)?"".concat(n.slice(0,e-3),"y"):"es"===n.slice(e-2,e)?n.slice(0,e-2):n.slice(0,e-1)}function x(){var n=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"";return p(b(n.toLowerCase()))}function w(n){var e,t=[["second",60],["minute",60],["hour",24],["day",7],["week",4],["month",12],["year",null]];return t.forEach((function(i,o){if(!e){var c=(0,r.Z)(i,2),u=c[0],l=c[1],a=t.slice(0,o).reduce((function(n,e){return n*Number(e[1])}),1);n<Number(l)*a&&(e=m(u,Math.round(n/a)))}})),e}function C(n){return!isNaN(n)}function j(n){var e,t=n.match(/\d+(\.?\d*)%/)||[];return Number(null===(e=t[0])||void 0===e?void 0:e.slice(0,-1))}function O(n){return"".concat(v(function(n){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:2;return Math.round((n||0)*Math.pow(100,e))/100}(n)),"%")}function A(n){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:2,t=Math.pow(10,e);return Math.round((n||0)*t)/t}function k(){return"".concat((0,l.mp)(i)," ").concat((0,l.mp)(c))}function E(){return"".concat((0,l.mp)(o)).concat((0,l.mp)(u))}},79274:function(n,e,t){(window.__NEXT_P=window.__NEXT_P||[]).push(["/pipelines",function(){return t(5545)}])}},function(n){n.O(0,[4259,2212,7689,1374,5763,6792,9774,2888,179],(function(){return e=79274,n(n.s=e);var e}));var e=n.O();_N_E=e}]);