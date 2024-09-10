document.addEventListener('DOMContentLoaded', function() {
  const buttons = document.querySelectorAll('.apply-button');

  buttons.forEach(button => {
    button.addEventListener('click', function() {
      const link = this.getAttribute('data-link');
      
      window.open(link, '_blank');
    });
  });
});

// Function to convert URLs in text to clickable links
function linkify(text) {
  const urlPattern = /(https?:\/\/\S+)/g;
  return text.replace(urlPattern, function(url) {
    return `<a href="${url}" target="_blank">${url}</a>`;
  });
}
