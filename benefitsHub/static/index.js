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

    const coverImages = [
        'assets/cover-images/cover-image_1.jpeg',
        'assets/cover-images/cover-image_2.jpeg',
        'assets/cover-images/cover-image_3.jpeg',
        'assets/cover-images/cover-image_4.jpeg',
        'assets/cover-images/cover-image_5.jpeg',
        'assets/cover-images/cover-image_6.jpeg',
        'assets/cover-images/cover-image_7.jpeg',
        'assets/cover-images/cover-image_8.jpeg',
    ];
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
    if (coverImages && coverImages.length > 0) {
        coverImageElement.src = coverImages[currentIndex];
    } else {
        console.error('No cover images available');
        return;
    }

    // Change image every 5 seconds
    let imageChangeInterval;
    try {
        imageChangeInterval = setInterval(changeCoverPhoto, 5000);
    } catch (error) {
        console.error('Error setting interval:', error);
    }

    // Add error handling for image loading
    coverImageElement.onerror = function() {
        console.error('Failed to load image:', coverImages[currentIndex]);
        currentIndex = (currentIndex + 1) % coverImages.length;
        coverImageElement.src = coverImages[currentIndex];
    };

    // Clean up interval on page unload
    window.addEventListener('unload', function() {
        if (imageChangeInterval) {
            clearInterval(imageChangeInterval);
        }
    });
});
