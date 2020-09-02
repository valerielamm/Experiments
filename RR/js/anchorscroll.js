function anchorScroll(target){
var element = document.querySelector(target)
var topPos = element.getBoundingClientRect().top + window.pageYOffset
window.scrollTo({
  top: topPos,
  behavior: 'smooth'
});}