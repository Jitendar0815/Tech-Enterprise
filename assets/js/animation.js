// Count-up animation for metric numbers
function animateValue(element, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        const current = Math.floor(progress * (end - start) + start);
        element.innerHTML = current + '%';
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

// Intersection Observer for count-up triggers
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const target = entry.target;
            const endVal = parseInt(target.getAttribute('data-end'));
            if (!isNaN(endVal) && !target.classList.contains('counted')) {
                target.classList.add('counted');
                animateValue(target, 0, endVal, 1500);
            }
        }
    });
}, { threshold: 0.5 });

// Observe all elements with class 'count-up'
document.querySelectorAll('.count-up').forEach(el => observer.observe(el));

// Typewriter effect
const textArray = [
    "Track audience retention millisecond by millisecond.",
    "Predict attention before you publish.",
    "Turn views into actionable insights."
];
let txtIndex = 0;
let charIndex = 0;
const typewriterEl = document.getElementById('typewriter');

function type() {
    if (!typewriterEl) return;
    if (charIndex < textArray[txtIndex].length) {
        typewriterEl.innerHTML += textArray[txtIndex].charAt(charIndex);
        charIndex++;
        setTimeout(type, 50);
    } else {
        setTimeout(erase, 2000);
    }
}

function erase() {
    if (!typewriterEl) return;
    if (charIndex > 0) {
        typewriterEl.innerHTML = textArray[txtIndex].substring(0, charIndex - 1);
        charIndex--;
        setTimeout(erase, 30);
    } else {
        txtIndex = (txtIndex + 1) % textArray.length;
        setTimeout(type, 500);
    }
}

// Start the typewriter on load
window.addEventListener('load', () => {
    setTimeout(type, 1000);
});
