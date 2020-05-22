"use strict";

const getAllCards = () => {
  $.get('/api/cards', (response) => {
    const cards = response.cards;
    const container = $('#container');

    // Empty container to flush old cards
    container.empty();

    for (const card of cards) {
      // Set placeholder image if card doesn't have an imgUrl
      if (!card.imgUrl) {

        card.imgUrl = `https://dummyimage.com/250x192/000/fff&text=${card.name}`;
      }

      container.append(`
        <div class="card">
          <p class="card-name">
            ${card.name}
          </p>

          <div class="card-img">
            <img src="${card.imgUrl}">
          </div>

          <p class="card-details">
            Skill: ${card.skill}
          </p>
        </div>
      `);
    }
  });
};


// Add a new card with info from form on submit
//
$('#new-card-form').on('submit', (evt) => {
  evt.preventDefault();

  const formData = {
    name: $('#name-field').val(),
    skill: $('#skill-field').val()
  };

  $.post('/api/cards', formData, (response) => {
    if (response.success) {
      // Success! We should retrieve the latest cards data
      getAllCards();
    } else {
      alert(`Oops, something went wrong. Error: ${response.error}`);
    }
  });
});
