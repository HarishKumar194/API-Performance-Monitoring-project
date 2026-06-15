import requests
import time

# APIs to test (intentionally includes a bad endpoint for realism)
apis = [
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/comments",
    "https://jsonplaceholder.typicode.com/invalid_endpoint"  # will fail
]

def test_api_performance(apis, runs=5):
    print("\nAPI Performance Monitoring System")
    print("----------------------------------\n")

    results = []

    for url in apis:
        times = []
        success = 0
        fail = 0

        print(f"Testing: {url}")

        for i in range(runs):
            try:
                start = time.time()
                response = requests.get(url, timeout=3)
                end = time.time()

                response_time = (end - start) * 1000  # ms
                times.append(response_time)

                if response.status_code == 200:
                    success += 1
                else:
                    fail += 1

                print(f" Run {i+1}: {response_time:.2f} ms | Status: {response.status_code}")

            except:
                fail += 1
                print(f" Run {i+1}: Failed (Timeout/Error)")

        avg_time = sum(times) / len(times) if times else 0
        success_rate = (success / runs) * 100
        fail_rate = (fail / runs) * 100

        results.append({
            "api": url,
            "avg_time": avg_time,
            "success_rate": success_rate,
            "fail_rate": fail_rate
        })

        print(f"\nAvg Response Time: {avg_time:.2f} ms")
        print(f"Success Rate: {success_rate:.2f}%")
        print(f"Failure Rate: {fail_rate:.2f}%\n")
        print("-" * 40)

    print("\nFINAL COMPARISON")
    print("----------------")

    for r in results:
        print(f"\n{r['api']}")
        print(f" Avg Time: {r['avg_time']:.2f} ms")
        print(f" Success: {r['success_rate']:.2f}% | Fail: {r['fail_rate']:.2f}%")

if __name__ == "__main__":
    test_api_performance(apis)
