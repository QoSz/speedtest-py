import speedtest

def run_speedtest():
    print("Running speed test...")
    s = speedtest.Speedtest()

    print("Getting best server based on ping...")
    best_server = s.get_best_server()
    print(f"Selected Server: {best_server['sponsor']} ({best_server['name']})")
    print(f"Location: {best_server['country']}, {best_server['cc']} - Distance: {best_server['d']} km")
    
    print("Performing download test...")
    download_speed = s.download() / 1_000_000  # Convert to Mbps
    print(f"Download speed: {download_speed:.2f} Mbps")

    print("Performing upload test...")
    upload_speed = s.upload() / 1_000_000  # Convert to Mbps
    print(f"Upload speed: {upload_speed:.2f} Mbps")

    print("Testing ping...")
    ping_result = s.results.ping
    print(f"Ping: {ping_result} ms")

if __name__ == "__main__":
    run_speedtest()
