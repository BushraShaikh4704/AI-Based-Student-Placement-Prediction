const branchSelect = document.getElementById("branch");

if (branchSelect) {

    const sections = {
        CSE: document.getElementById("cse-skills"),
        IT: document.getElementById("it-skills"),
        ECE: document.getElementById("ece-skills"),
        EE: document.getElementById("ee-skills"),
        ME: document.getElementById("me-skills"),
        CE: document.getElementById("ce-skills"),
        Chemical: document.getElementById("chemical-skills")
    };

    function updateSkills() {

        Object.values(sections).forEach(section => {
            section.style.display = "none";
        });

        sections[branchSelect.value].style.display = "block";
    }

    branchSelect.addEventListener("change", updateSkills);

    updateSkills();
}