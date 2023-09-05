[BITS 16]

start:
    ; Set up segment registers
    xor ax, ax
    mov ds, ax
    mov es, ax

    ; Load the kernel into memory
    mov bx, 0x1000  ; Destination address in memory
    mov ah, 0x02    ; Function number for disk read
    mov al, 1       ; Number of sectors to read
    mov ch, 0       ; Cylinder number
    mov cl, 2       ; Sector number
    mov dh, 0       ; Head number
    mov dl, 0       ; Drive number (0 = first floppy drive)

    int 0x13        ; BIOS interrupt to read disk

    ; Jump to the loaded kernel
    jmp 0x1000:0x0000

    ; Padding and magic number
    times 510-($-$$) db 0
    dw 0xAA55