document.addEventListener("DOMContentLoaded", function () {
  const slider = document.querySelector(".slider");
  const slides = document.querySelectorAll(".slide");
  let currentSlide = 0;

  function showSlide() {
    slider.style.transform = `translateX(-${currentSlide * 100}%)`;
  }

  function nextSlide() {
    if (currentSlide < slides.length - 1) {
      currentSlide++;
      showSlide();
    }
  }

  function prevSlide() {
    if (currentSlide > 0) {
      currentSlide--;
      showSlide();
    }
  }

  document.querySelector(".next").addEventListener("click", nextSlide);
  document.querySelector(".prev").addEventListener("click", prevSlide);
});
const textInputs = document.querySelectorAll(".text-input");
const selectBoxes = document.querySelectorAll(".select-box");
const radioBtns = document.querySelectorAll(".radio-btn");
const progressBar = document.getElementById("progress");
const questions = document.querySelectorAll(".question");

const totalQuestions = questions.length;

let filledInputs = 0;

function updateProgressBar() {
  const progressPercentage = (filledInputs / totalQuestions) * 100;
  progressBar.style.width = `${progressPercentage}%`;
}

function checkFilledInputs() {
  filledInputs = 0;
  textInputs.forEach((input) => {
    if (input.value.length >= 3) filledInputs++;
  });
  selectBoxes.forEach((select) => {
    if (select.value !== "") filledInputs++;
    console.log(selectBoxes);
  });
  radioBtns.forEach((radio) => {
    if (radio.checked) filledInputs++;
  });
  updateProgressBar();
}

textInputs.forEach((input) => {
  input.addEventListener("input", checkFilledInputs);
});

selectBoxes.forEach((select) => {
  select.addEventListener("change", checkFilledInputs);
});

radioBtns.forEach((radio) => {
  radio.addEventListener("change", checkFilledInputs);
});

var dropdown = document.getElementsByClassName("dropdown")[0];
var btn = document.getElementsByClassName("dropdown-button")[0];

btn.addEventListener("click", function () {
  dropdown.classList.toggle("active");
});
