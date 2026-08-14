#include <SDL3/SDL.h>
#include <iostream>

int main() {
    SDL_SetHint(SDL_HINT_VIDEO_DRIVER, "dummy");
    SDL_SetHint(SDL_HINT_JOYSTICK_ALLOW_BACKGROUND_EVENTS, "1");

    SDL_Init(SDL_INIT_VIDEO | SDL_INIT_GAMEPAD | SDL_INIT_EVENTS);

    SDL_Window * window = SDL_CreateWindow("Mocha", 100, 100, SDL_WINDOW_HIDDEN);
    SDL_Event event;
    bool running = true;
    SDL_Gamepad * gamepad;

    const Uint64 fps = 60;
    const Uint64 frame_ms = 1000 / fps;
    Uint64 start;
    Uint64 time;

    int button = -1;


    while (running) {
        start = SDL_GetTicks();

        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_EVENT_QUIT) running = false;
            if (event.type == SDL_EVENT_GAMEPAD_ADDED) {
                gamepad = SDL_OpenGamepad(event.gdevice.which);
                if (!gamepad) {
                    SDL_Log("Failed gamepad open");
                    return 0;
                }
                SDL_Log("Gamepad added: %s", SDL_GetGamepadName(gamepad));
            }
        }

        if (gamepad && SDL_GetGamepadButton(gamepad, SDL_GAMEPAD_BUTTON_SOUTH)) {
            if (button != SDL_GAMEPAD_BUTTON_SOUTH) {
                button = SDL_GAMEPAD_BUTTON_SOUTH;
                std::cout << "A" << std::endl;
            }
        }

        if (gamepad && SDL_GetGamepadButton(gamepad, SDL_GAMEPAD_BUTTON_NORTH)) {
            if (button != SDL_GAMEPAD_BUTTON_NORTH) {
                button = SDL_GAMEPAD_BUTTON_NORTH;
                std::cout << "Y" << std::endl;
            }
        }

        if (gamepad && SDL_GetGamepadButton(gamepad, SDL_GAMEPAD_BUTTON_EAST)) {
            if (button != SDL_GAMEPAD_BUTTON_EAST) {
                button = SDL_GAMEPAD_BUTTON_EAST;
                std::cout << "B" << std::endl;
            }
        }

        if (gamepad && SDL_GetGamepadButton(gamepad, SDL_GAMEPAD_BUTTON_WEST)) {
            if (button != SDL_GAMEPAD_BUTTON_WEST) {
                button = SDL_GAMEPAD_BUTTON_WEST;
                std::cout << "X" << std::endl;
            }
        }

        time = SDL_GetTicks() - start;
        if (time < frame_ms) {
            SDL_Delay(frame_ms - time);
        }
    }

    return 1;
}