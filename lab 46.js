const imageUrls = [
  'https://picsum.photos/id/1011/600/400',
  'https://picsum.photos/id/1012/600/400',
  'https://picsum.photos/id/1015/600/400',
  'https://picsum.photos/id/1020/600/400',
  'https://picsum.photos/id/1025/600/400',
  'https://picsum.photos/id/1035/600/400'
];

const gallery = document.querySelector('.gallery');
const modal = document.querySelector('.modal');
const modalImg = document.querySelector('.modal-img');
const closeBtn = document.querySelector('.close');
const prevBtn = document.getElementById('prev');
const nextBtn = document.getElementById('next');

let currentIndex = 0;

// Generate Gallery Dynamically
imageUrls.forEach((url, index) => {
  const img = document.createElement('img');
  img.src = url;
  img.dataset.index = index;
  gallery.appendChild(img);
});

// Open Modal
gallery.addEventListener('click', (e) => {
  if (e.target.tagName === 'IMG') {
    currentIndex = +e.target.dataset.index;
    openModal(currentIndex);
  }
});

function openModal(index) {
  modal.classList.remove('hidden');
  modalImg.src = imageUrls[index];
  modalImg.style.transform = 'scale(1)';
  localStorage.setItem('lastImage', index);
}

// Close Modal
function closeModal() {
  modal.classList.add('hidden');
}

// Click outside image or on close
modal.addEventListener('click', (e) => {
  if (e.target === modal || e.target === closeBtn) {
    closeModal();
  }
});

// Navigation
nextBtn.addEventListener('click', () => {
  currentIndex = (currentIndex + 1) % imageUrls.length;
  animateImageChange();
});

prevBtn.addEventListener('click', () => {
  currentIndex = (currentIndex - 1 + imageUrls.length) % imageUrls.length;
  animateImageChange();
});

// Animate image switch
function animateImageChange() {
  modalImg.style.transform = 'scale(0.8)';
  setTimeout(() => {
    modalImg.src = imageUrls[currentIndex];
    modalImg.style.transform = 'scale(1)';
    localStorage.setItem('lastImage', currentIndex);
  }, 200);
}

// Bonus: Restore last image
window.addEventListener('load', () => {
  const lastIndex = localStorage.getItem('lastImage');
  if (lastIndex !== null) {
    currentIndex = +lastIndex;
    openModal(currentIndex);
  }
});
