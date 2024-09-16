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

document.addEventListener('DOMContentLoaded', function () {
  const coverImageElement = document.getElementById('coverImage');
  if (!coverImageElement) {
      console.error('Cover image element not found');
      return;
  }

  let currentIndex = 0;
  function changeCoverPhoto() {
      if (!coverImageElement) return;

      coverImageElement.style.opacity = '0';
      
      setTimeout(() => {
          currentIndex = (currentIndex + 1) % coverImages.length;
          coverImageElement.src = coverImages[currentIndex];
          coverImageElement.style.opacity = '1';
      }, 500);
  }

  // Set initial image
  // Check if coverImages is defined in the global scope
  if (typeof coverImages !== 'undefined' && Array.isArray(coverImages) && coverImages.length > 0) {
      coverImageElement.src = coverImages[currentIndex];
  } else {
      console.error('coverImages is not defined or is empty');
      // Fallback to a default image or handle the error as needed
      coverImageElement.src = '/static/assets/cover-images/cover-image_1.jpeg'; // Adjust the path as necessary
      return;
  }

  // Change image every 5 seconds
  let imageChangeInterval = setInterval(changeCoverPhoto, 5000);

  // Add error handling for image loading
  coverImageElement.onerror = function() {
      console.error('Failed to load image:', coverImages[currentIndex]);
      currentIndex = (currentIndex + 1) % coverImages.length;
      coverImageElement.src = coverImages[currentIndex];
  };

  // Clean up interval on page unload
  window.addEventListener('unload', function() {
      clearInterval(imageChangeInterval);
  });
});