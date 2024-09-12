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

// Simulate loading time or condition
setTimeout(function() {
    document.getElementById('splash-screen').style.display = 'none';
    document.getElementById('container').style.display = 'block';
}, 5000); // Change to desired time or loading condition

// document.addEventListener('DOMContentLoaded', function () {
//     // Array of image paths
//     const coverImages = [
//         "{{ url_for('static', filename='assets/cover-images/cover-image_1.jpeg') }}",
//         "{{ url_for('static', filename='assets/cover-images/cover-image_2.jpeg') }}",
//         "{{ url_for('static', filename='assets/cover-images/cover-image_3.jpeg') }}",
//         "{{ url_for('static', filename='assets/cover-images/cover-image_4.jpeg') }}",
//         "{{ url_for('static', filename='assets/cover-images/cover-image_5.jpeg') }}",
//         "{{ url_for('static', filename='assets/cover-images/cover-image_6.jpeg') }}",
//         "{{ url_for('static', filename='assets/cover-images/cover-image_7.jpeg') }}",
//         "{{ url_for('static', filename='assets/cover-images/cover-image_8.jpeg') }}",
//     ];

//     // Get the image element
//     const coverImageElement = document.getElementById('coverImage');

//     coverImageElement.src = coverImages[0]
//     // Start with the first image
//     let currentIndex = 0;

//     // Function to change the image
//     function changeImage() {
//         currentIndex = (currentIndex + 1) % coverImages.length; // Cycle through the array
//         coverImageElement.src = coverImages[currentIndex];      // Update the image source
//     }

//     // Change image every 5 seconds (5000 ms)
//     setInterval(changeImage, 5000);
// });
