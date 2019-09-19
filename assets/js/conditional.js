window.onload = function() {
    const checkbox = document.getElementById('id_is_checked');
    const student = document.getElementById('id_student');
    const student_section = document.getElementsByClassName("form-row field-student")[0];

    checkbox.addEventListener('change', (event) => {
      if (event.target.checked) {
        student_section.style.display = 'none';
        student.value = 2
      } else {
        student_section.style.display = 'block';
      }
    })
}