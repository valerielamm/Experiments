<?php
/*
Plugin Name: The Weather
Description: Tell the world what the weather is like where you live.
Author: Valerie Lamm
Author URI: https://github.com/valerielamm
Version: 1.0
*/


/* Define */
define( 'THE_WEATHER_URL', WP_PLUGIN_URL . '/' . plugin_basename( dirname( __FILE__ ) ) . '/' );

/* Including files */
require_once("inc/scripts.php");
require_once("inc/widget.php");