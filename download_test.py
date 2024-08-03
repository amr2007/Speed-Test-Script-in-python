# Import the speedtest module
import speedtest
 
def Download():
    # Initialize the Speedtest class
    st = speedtest.Speedtest()

    # Find the best server based on ping
    print("Finding the best server...")
    best = st.get_best_server()
    print(f"We found the best server: {best}")

    # Perform a download speed test
    download_result = st.download()
    # Convert the result from bits per second to megabytes per second and round to 2 decimal places
    print(f"The download speed: {round(download_result / 1024**2 / 8, 2)} Mbps")

# Call the Download function to run the speed test
Download()
