"use strict";

// Loading Bar One
function fillBar(seconds) {
  var bar = document.querySelector('.bar');
  bar.style.transition = seconds + 's linear width';
  bar.style.width = '100%';
} 

// Loading Bar Two
function fillBarTwo(seconds) {
  var bar = document.querySelector('.bar-two');
  var atPercent = 0;
  var interval = setInterval(function () {
    atPercent++;
    bar.style.width = atPercent + '%';
    console.log('running at', atPercent);

    if (atPercent >= 100) {
      clearInterval(interval);
    }
  }, seconds * 1000 / 100);
}