// jQuery Customization from Materialize:
// https://materializecss.com/
$(document).ready(function(){
    // Mobile hamburger navbar
    $('.sidenav').sidenav({edge: "right"});
    // Collapsible accordion list
    $('.collapsible').collapsible();
    // Dataset list > "To Do" Tooltip
    $('.tooltipped').tooltip();
    // Category Selection > Add New Dataset form
    $('select').formSelect();
    // DatePicker > Add New Dataset form
    $(document).ready(function(){
        $('.datepicker').datepicker({
            format: "dd mmmm, yyyy",
            yearRange: 3,
            showClearBtn: true,
            i18n: {
                done: "Select"
            }
        });
    }); 
});