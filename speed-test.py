import speedtest

def test_internet_speed():
    """
    Measures and displays the internet download, upload, and ping speeds.
    """
    try:
        print("Initializing speed test...")
        st = speedtest.Speedtest()

        print("Finding best server...")
        st.get_best_server()  # Selects the optimal server for testing

        print("Performing download test...")
        download_speed_bps = st.download()  # Speed in bits per second
        download_speed_mbps = download_speed_bps / 1_000_000  # Convert to Mbps

        print("Performing upload test...")
        upload_speed_bps = st.upload()  # Speed in bits per second
        upload_speed_mbps = upload_speed_bps / 1_000_000  # Convert to Mbps

        ping = st.results.ping  # Ping in milliseconds

        print("\n--- Speed Test Results ---")
        print(f"Download Speed: {download_speed_mbps:.2f} Mbps")
        print(f"Upload Speed: {upload_speed_mbps:.2f} Mbps")
        print(f"Ping: {ping:.2f} ms")

    except speedtest.SpeedtestException as e:
        print(f"An error occurred during the speed test: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    test_internet_speed()
