const ob = document.querySelector('body')
ob.addEventListener('click', e => {
  const o = e.target.closest('.mybutt')
  if (!o) {
    if (e.target.closest('.content')) return
    ob.querySelectorAll('.content.show').forEach(el => animateDisplay(el, 'show', 'block', 300))
    return
  }
  const op = e.target.closest('.container')
  const el = op.querySelector('.content')
  animateDisplay(el, 'show', 'block', 300)
});

function animateDisplay(target, animationClass, displayType, timeout) {
  // timeout should be longer than css transition
  var doneTimedDisplay = false,
    displaying = false;

  target.addEventListener('transitionend', function() {
    if (!target.classList.contains('show')) {
      target.style.display = 'none';
    }
    doneTimedDisplay = true;
  });
  if (!target.style.display || target.style.display === 'none') {
    displaying = true;
    target.style.display = displayType;
  } else {
    displaying = false;
  }

  setTimeout(function() {
    target.classList.toggle(animationClass);
    doneTimedDisplay = false;
  }, 10);

  if (!displaying) {
    setTimeout(function() {
      // failsafe for transitioned not firing
      if (!doneTimedDisplay) {
        target.style.display = 'none';
      }
      doneTimedDisplay = true;
    }, timeout);
  }
};