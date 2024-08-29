const buttons = document.querySelectorAll('.apply-button');

buttons.forEach(button => { 
  button.addEventListener('click', function() {
  const link = this.getAttribute('data-link');
  window.open(link, '_blank');
  });
});