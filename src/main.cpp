
#include <stdio.h>
#include "pico/stdlib.h"
#include "FreeRTOS.h"
#include "task.h"

void led_task(void *pvp)
{
    const uint LED_PIN = PICO_DEFAULT_LED_PIN;
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);
    while (true)
    {
        printf("Led On\n");
        gpio_put(LED_PIN, 1);
        vTaskDelay(1000);
        gpio_put(LED_PIN, 0);
        printf("Led Off\n");
        vTaskDelay(1000);
        
    }
}

extern "C" int main()
{
    stdio_init_all();

    xTaskCreate(&led_task, "LED_Task", 256, nullptr, 1, nullptr);
    vTaskStartScheduler();

    while (1)
    {
    };
}