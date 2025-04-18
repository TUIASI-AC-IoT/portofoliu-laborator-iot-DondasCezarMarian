/*  WiFi softAP Example

   This example code is in the Public Domain (or CC0 licensed, at your option.)

   Unless required by applicable law or agreed to in writing, this
   software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
   CONDITIONS OF ANY KIND, either express or implied.
*/
#include <string.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_system.h"
#include "esp_wifi.h"
#include "esp_event.h"
#include "esp_log.h"
#include "nvs_flash.h"
#include "freertos/event_groups.h"
#include "esp_http_server.h"


#include "lwip/err.h"
#include "lwip/sys.h"

#include "soft-ap.h"
#include "http-server.h"

#include "../mdns/include/mdns.h"
void start_mdns_service(void)
{
    //initialize mDNS service
    esp_err_t err = mdns_init();
    if (err) {
        ESP_LOGI("","MDNS Init failed: %d\n", err);
        return;
    }

    //set hostname
    mdns_hostname_set("esp32-Dondas");
    //set default instance
    mdns_instance_name_set("Cezar's ESP32 Thing");
}

void app_main(void)
{
    //Initialize NVS
    esp_err_t ret = nvs_flash_init();
    if (ret == ESP_ERR_NVS_NO_FREE_PAGES || ret == ESP_ERR_NVS_NEW_VERSION_FOUND) {
      ESP_ERROR_CHECK(nvs_flash_erase());
      ret = nvs_flash_init();
    }
    ESP_ERROR_CHECK(ret);
    wifi_init_softap();
    //start_mdns_service();
    // TODO: 3. Pornire mod STA + scanare SSID-uri disponibile

    // TODO: 4. Initializare mDNS (daca mai ramana timp)    

    // TODO: 1. Pornire softAP

    // TODO: 2. Pornire server web (si config specifice in http-server.c) 
}