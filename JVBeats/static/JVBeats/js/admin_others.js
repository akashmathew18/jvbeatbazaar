document.addEventListener('DOMContentLoaded', function () {
    const genreField = document.querySelector('#id_genre');
    const categoryField = document.querySelector('#id_category');
    const customGenreField = document.querySelector('#id_custom_genre');
    const customCategoryField = document.querySelector('#id_custom_category');

    function toggleCustomField(dropdown, customField) {
        if (dropdown.value === 'others') {
            customField.parentElement.style.display = 'block';
        } else {
            customField.parentElement.style.display = 'none';
            customField.value = ''; // Clear the input
        }
    }

    // Initial state
    toggleCustomField(genreField, customGenreField);
    toggleCustomField(categoryField, customCategoryField);

    // Event listeners
    genreField.addEventListener('change', () => toggleCustomField(genreField, customGenreField));
    categoryField.addEventListener('change', () => toggleCustomField(categoryField, customCategoryField));
});
