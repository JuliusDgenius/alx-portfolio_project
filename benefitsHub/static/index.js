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
    // Array of image paths
    // const coverImages = [
    //     "{{ url_for('static', filename='assets/cover-images/cover-image_1.jpeg') }}",
    //     "{{ url_for('static', filename='assets/cover-images/cover-image_2.jpeg') }}",
    //     "{{ url_for('static', filename='assets/cover-images/cover-image_3.jpeg') }}",
    //     "{{ url_for('static', filename='assets/cover-images/cover-image_4.jpeg') }}",
    //     "{{ url_for('static', filename='assets/cover-images/cover-image_5.jpeg') }}",
    //     "{{ url_for('static', filename='assets/cover-images/cover-image_6.jpeg') }}",
    //     "{{ url_for('static', filename='assets/cover-images/cover-image_7.jpeg') }}",
    //     "{{ url_for('static', filename='assets/cover-images/cover-image_8.jpeg') }}",
    // ];

    const coverImageElement = document.getElementById('coverImage');
    let currentIndex = 0;

    function changeCoverPhoto() {
        coverImageElement.style.opacity = 0;
        
        setTimeout(() => {
            currentIndex = (currentIndex + 1) % coverImages.length;
            coverImageElement.src = coverImages[currentIndex];
            coverImageElement.style.opacity = 1;
        }, 500); // Changed from 5000 to 500 for a smoother transition
    }

    // Set initial image
    if (coverImages && coverImages.length > 0) {
        coverImageElement.src = coverImages[currentIndex];
    } else {
        console.error('No cover images available');
    }

    // Change image every 5 seconds
    const imageChangeInterval = setInterval(changeCoverPhoto, 5000);

    // Add error handling for image loading
    coverImageElement.onerror = function() {
        console.error('Failed to load image:', coverImages[currentIndex]);
        changeCoverPhoto(); // Skip to next image if current one fails to load
    };

    // Clean up interval on page unload
    window.addEventListener('unload', function() {
        clearInterval(imageChangeInterval);
    });
});
