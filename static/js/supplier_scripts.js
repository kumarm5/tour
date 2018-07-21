$(document).ready(function(){

    trip_type_content = function(){
        trip_type = $('#id_triptype option:selected').text();
        
        if(trip_type == 'Round Trip'){
            console.log('Round Trip');
            // one way trip
            $('.field-oneway_date').parent('.form-row').hide();
            $('.field-oneway_seat_availability').parent('.form-row').hide();
            $('#id_oneway_time').parent().parent().hide();

            // round trip
            $('.field-departure_time').parent('.form-row').show();
            $('.field-return_flt_no').parent('.form-row').show();
            $('.field-total_departure_seats').parent('.form-row').show();
            $('.field-return_seat_availability').parent('.form-row').show();
            $('.field-dep_rate_supplier').parent('.form-row').show();

        }else {
            console.log('One Way');
            // one way trip
            $('.field-oneway_date').parent('.form-row').show();
            $('.field-oneway_seat_availability').parent('.form-row').show();
            $('#id_oneway_time').parent().parent().show();

            // round trip
            $('.field-departure_time').parent('.form-row').hide();
            $('.field-return_flt_no').parent('.form-row').hide();
            $('.field-total_departure_seats').parent('.form-row').hide();
            $('.field-return_seat_availability').parent('.form-row').hide();
            $('.field-dep_rate_supplier').parent('.form-row').hide();            
        }
    }
    
    // change event of id trip type
    $('#id_triptype').on('change', function(){
        trip_type_content();        
    }); 

    
});