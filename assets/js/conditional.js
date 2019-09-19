window.onload = function() {
    const checkbox = document.getElementById('id_is_checked');
    const student = document.getElementById('id_student');
    const student_section = document.getElementsByClassName("form-row field-student");

    checkbox.addEventListener('change', (event) => {
      if (event.target.checked) {
        student.style.display = 'none';
      } else {
        student.style.display = 'block';
      }
    })
}