from APP import create_app

if __name__ == "__main__":
    # Crear la aplicación Flask
    app = create_app()

    # Definir el puerto y el esquema
    port = 5000  # Puerto por defecto
    scheme = 'http'  # Esquema por defecto

    # Ejecutar la aplicación Flask
    app.run(port=port, debug=True)
