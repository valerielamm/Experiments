var container = document.getElementById("container");
function flexboxChange(styleChange){
    switch(styleChange){
        case flex:
            container.style.display = "flex";
            
            break;
        case inlineFlex:
            container.style.display = "inline-flex";
            break;
        case row:
            container.style.flexDirection = "row";
            break;
        case rowReverse:
            container.style.flexDirection = "row-reverse";
            break;
        case column:
            container.style.flexDirection = "column";
            break;
        case columnReverse:
            container.style.flexDirection = "column-reverse";
            break;
        case nowrap:
            container.style.flexWrap = "nowrap";
            break;
        case wrap:
            container.style.flexWrap = "wrap";
            break;
        case wrapReverse:
            container.style.flexWrap = "wrap-reverse";
            break;
        case justifyFlexStart:
            container.style.justifyContent = "flex-start";
            break;
        case justifyFlexEnd:
            container.style.justifyContent = "flex-end";
            break;
        case justifyCenter:
            container.style.justifyContent = "center";
            break;
        case justifySpaceBetween:
            container.style.justifyContent = "space-between";
            break;
        case justifySpaceAround:
            container.style.justifyContent = "space-around";
            break;
        case itemsFlexStart:
            container.style.alignItems = "flex-start";
            break;
        case itemsFlexEnd:
            container.style.alignItems = "flex-end";
            break;
        case itemsCenter:
            container.style.alignItems = "center";
            break;
        case itemsBaseline:
            container.style.alignItems = "baseline";
            break;
        case itemsStretch:
            container.style.alignItems = "stretch";
            break;
        case contentFlexStart:
            container.style.alignContent = "flex-start";
            break;
        case contentFlexEnd:
            container.style.alignContent = "flex-end";
            break;
        case contentCenter:
            container.style.alignContent = "center";
            break;
        case contentSpaceBetween:
            container.style.alignContent = "space-between";
            break;
        case contentSpaceAround:
            container.style.alignContent = "space-around";
            break;
        case contentStretch:
            container.style.alignContent = "stretch";
            break;
        default:
            console.log("flexbox error");
            break;
    }
}
var divCount = 3;
function moreDivs(){
    var div = document.createElement("div");
    div.innerHTML = divCount+1;
    div.className = "box";
    container.appendChild(div);
    divCount++;
}

function lessDivs(){
    if (divCount > 1){
        let item = container.lastElementChild;
        container.removeChild(item);
        divCount--;
    };
}
