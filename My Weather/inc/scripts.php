<?php

if ( ! defined( 'ABSPATH' ) ) exit; // Exit if accessed directly

/*** Plugin Scripts and CSS ***/
if (!function_exists('sp_location_weather_scripts_and_style')) {
	function sp_location_weather_scripts_and_style(){
		// CSS Files
		wp_enqueue_style('location-weather-style', THE_WEATHER_URL . 'assets/css/style.css');

		//JS Files
		wp_enqueue_script( 'location-weather-min-js', THE_WEATHER_URL . 'assets/js/Weather.min.js', array('jquery'), NULL, TRUE );
	}
	add_action('wp_enqueue_scripts', 'sp_location_weather_scripts_and_style');
}


