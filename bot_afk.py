import time
import ctypes

def prevent_sleep():
    print("Bot de prevenção de suspensão ativado.")
    # Define o tempo em que o sistema permanecerá ativo antes de reiniciar o contador.
    # O valor padrão é 5 segundos.
    time_interval = 5

    while True:
        # Verifica se o sistema está bloqueado (tela de login) ou desbloqueado (ativo).
        locked = ctypes.windll.user32.GetForegroundWindow() == 0

        # Se o sistema estiver desbloqueado, simula uma atividade de teclado
        # para evitar que o Windows entre no modo de suspensão.
        if not locked:
            # Use esse código para simular um pressionamento de tecla (tecla F15).
            # Isso evita que o Windows entre no modo de suspensão.
            ctypes.windll.user32.keybd_event(0x7E, 0, 0, 0)  # Pressionar a tecla
            ctypes.windll.user32.keybd_event(0x7E, 0, 0x2, 0)  # Liberar a tecla

        # Espera por um intervalo antes de verificar novamente.
        time.sleep(time_interval)

if __name__ == "__main__":
    try:
        prevent_sleep()
    except KeyboardInterrupt:
        pass
