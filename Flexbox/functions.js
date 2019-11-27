var container = document.getElementById("container");

/*
    Button groups for the #container div.
    They are grouped together under the property they belong to.
    This is used to quickly remove the 'selected' class from 
    all related buttons when there is a change to their property.
*/
var displays = document.querySelectorAll('#flex, #inlineFlex');
var flexDirections = document.querySelectorAll('#row, #rowReverse, #column, #columnReverse');
var flexWraps = document.querySelectorAll('#nowrap, #wrap, #wrapReverse');
var justifyContents = document.querySelectorAll('#justifyFlexStart, #justifyFlexEnd, #justifyCenter, #justifySpaceBetween, #justifySpaceAround');
var alignItems = document.querySelectorAll('#itemsFlexStart, #itemsFlexEnd, #itemsCenter, #itemsBaseline, #itemsStretch');
var alignContents = document.querySelectorAll('#contentFlexStart, #contentFlexEnd, #contentCenter, #contentSpaceBetween, #contentSpaceAround, #contentStretch');

// Turn all buttons 'off' and then the selected one 'on' (in it's property group)
function greyButtons(groupName, selected) {
    for (var i = 0; i < groupName.length; i++) {
        groupName[i].classList.remove("selected");
    };
    document.getElementById(selected).classList.add("selected");
}

// Called when a property change button is pressed
function flexboxChange(styleChange) {
    switch (styleChange) {
        case flex:
            container.style.display = "flex";
            greyButtons(displays, "flex");
            break;
        case inlineFlex:
            container.style.display = "inline-flex";
            greyButtons(displays, "inlineFlex");
            break;
        case row:
            container.style.flexDirection = "row";
            greyButtons(flexDirections, "row");
            break;
        case rowReverse:
            container.style.flexDirection = "row-reverse";
            greyButtons(flexDirections, "rowReverse");
            break;
        case column:
            container.style.flexDirection = "column";
            greyButtons(flexDirections, "column");
            break;
        case columnReverse:
            container.style.flexDirection = "column-reverse";
            greyButtons(flexDirections, "columnReverse");
            break;
        case nowrap:
            container.style.flexWrap = "nowrap";
            greyButtons(flexWraps, "nowrap");
            break;
        case wrap:
            container.style.flexWrap = "wrap";
            greyButtons(flexWraps, "wrap");
            break;
        case wrapReverse:
            container.style.flexWrap = "wrap-reverse";
            greyButtons(flexWraps, "wrapReverse");
            break;
        case justifyFlexStart:
            container.style.justifyContent = "flex-start";
            greyButtons(justifyContents, "justifyFlexStart");
            break;
        case justifyFlexEnd:
            container.style.justifyContent = "flex-end";
            greyButtons(justifyContents, "justifyFlexEnd");
            break;
        case justifyCenter:
            container.style.justifyContent = "center";
            greyButtons(justifyContents, "justifyCenter");
            break;
        case justifySpaceBetween:
            container.style.justifyContent = "space-between";
            greyButtons(justifyContents, "justifySpaceBetween");
            break;
        case justifySpaceAround:
            container.style.justifyContent = "space-around";
            greyButtons(justifyContents, "justifySpaceAround");
            break;
        case itemsFlexStart:
            container.style.alignItems = "flex-start";
            greyButtons(alignItems, "itemsFlexStart");
            break;
        case itemsFlexEnd:
            container.style.alignItems = "flex-end";
            greyButtons(alignItems, "itemsFlexEnd");
            break;
        case itemsCenter:
            container.style.alignItems = "center";
            greyButtons(alignItems, "itemsCenter");
            break;
        case itemsBaseline:
            container.style.alignItems = "baseline";
            greyButtons(alignItems, "itemsBaseline");
            break;
        case itemsStretch:
            container.style.alignItems = "stretch";
            greyButtons(alignItems, "itemsStretch");
            break;
        case contentFlexStart:
            container.style.alignContent = "flex-start";
            greyButtons(alignContents, "contentFlexStart");
            break;
        case contentFlexEnd:
            container.style.alignContent = "flex-end";
            greyButtons(alignContents, "contentFlexEnd");
            break;
        case contentCenter:
            container.style.alignContent = "center";
            greyButtons(alignContents, "contentCenter");
            break;
        case contentSpaceBetween:
            container.style.alignContent = "space-between";
            greyButtons(alignContents, "contentSpaceBetween");
            break;
        case contentSpaceAround:
            container.style.alignContent = "space-around";
            greyButtons(alignContents, "contentSpaceAround");
            break;
        case contentStretch:
            container.style.alignContent = "stretch";
            greyButtons(alignContents, "contentStretch");
            break;
        default:
            console.log("flexbox error");
            break;
    }
}

// Used to randomize shades of grey on new divs
function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
}

// Number count on divs
var divCount = 3;

// Add another 'box' div to #container
function moreDivs() {
    var div = document.createElement("div");
    div.innerHTML = divCount + 1;
    div.className = "box";
    div.style.background = "rgba(255, 255, 255, ." + getRandomInt(5) + ")";
    container.appendChild(div);
    divCount++;
}

// Remove the last 'box' div from #container
function lessDivs() {
    if (divCount > 1) {
        let item = container.lastElementChild;
        container.removeChild(item);
        divCount--;
    };
}
