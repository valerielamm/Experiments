function reviewViewMore(thisObject) {
  var more_text = document.createTextNode("more");
  var collapse_text = document.createTextNode("collapse");
  // shows more text if collapsed 
  if (thisObject.classList.contains('collapsed')) {
    thisObject.parentElement.parentElement.querySelector('.review-summary').style.height = "auto";
    // wont cover last words to the left of 'collapse' if they reach the end
    thisObject.parentElement.parentElement.style.paddingBottom = "2em";
    thisObject.classList.remove('collapsed');
    thisObject.classList.add('showing-more');
  }
  // hides text if showing more
  else if (thisObject.classList.contains('showing-more')) {
    thisObject.parentElement.parentElement.querySelector('.review-summary').style.height = "3em";
    thisObject.parentElement.parentElement.style.paddingBottom = "0";
    thisObject.classList.add('collapsed');
    thisObject.classList.remove('showing-more');
  }
  // resets
  else {
    console.log('ono toggling the more button is not working');
  }

}