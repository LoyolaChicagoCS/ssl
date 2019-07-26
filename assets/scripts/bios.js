document.addEventListener("DOMContentLoaded", () => {
    const team = [
        'allan',
        'zac',
        'riley',
        'morgan',
        'sean',
        'jack',
        'jonathan',
        'emmanuel',
        'linette',
        'george',
        'gregory',
        'konstantin',
        'shilpika',
        'davidw',
        'neil'
    ];

    displayBioOnClick(team);

    function displayBioOnClick(team) {
        for (let person of team) {
            let personPhoto = document.getElementById(person);
            const personBio = document.getElementById(`${person}-description`);

            console.log(personBio);

            personPhoto.addEventListener('click', () => {
                if (personBio.style.display === 'block') {
                    personBio.style.display = 'none';
                } else {
                    personBio.style.display = 'block';
                }
            });

            window.addEventListener('click', (event) => {
                if (event.target !== personPhoto) {
                    personBio.style.display = 'none';
                }
            });
        }
    }
});
