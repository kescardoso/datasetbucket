// jQuery Customization from Materialize:
// https://materializecss.com/

$(document).ready(function(){

    // Mobile hamburger navbar
    $('.sidenav').sidenav({
        edge: "right"
    });

    // Navbar dropdown
    $(".dropdown-trigger").dropdown({
        constrainWidth: false,
        coverTrigger: false,
        alignment: 'center'
    });

    // Dataset List : collapsible accordion
    $('.collapsible').collapsible();

    // Dataset list > "To Do" Tooltip
    $('.tooltipped').tooltip();

    // DatePicker > Add/Edit Dataset form
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });

    // Select Categories > Add/Edit Dataset form
    $('select').formSelect();
});

// Upload progress bar > Analyse form
$('#analyse_btn').click(function(){
    $('#progress_bar').html('<div class="progress"><div class="indeterminate"></div></div>')
});