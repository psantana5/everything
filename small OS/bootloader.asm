BITS 16

start:
    ; Configurar registros de segmento
    xor ax, ax
    mov ds, ax
    mov es, ax

    ; Configurar la pila
    mov ax, 0x9000
    mov ss, ax
    mov sp, 0xFFFF

    ; Cargar el kernel en memoria
    mov bx, 0x1000  ; Dirección de destino en memoria
    mov ah, 0x02    ; Número de función para leer disco
    mov al, 1       ; Número de sectores a leer
    mov ch, 0       ; Número de cilindro
    mov cl, 2       ; Número de sector
    mov dh, 0       ; Número de cabeza
    mov dl, 0       ; Número de unidad de disco (0 = primera unidad de disquete)

    int 0x13        ; Interrupción de BIOS para leer disco

    ; Saltar al kernel cargado
    jmp 0x1000:0x0000

    ; Relleno y número mágico
    times 510-($-$$) db 0
    dw 0xAA55