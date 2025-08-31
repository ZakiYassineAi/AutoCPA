import time
import random

class AnalyticsAgent:
    def __init__(self):
        print("Initializing Analytics Agent...")
        self.daily_performance = {
            'views': 0,
            'clicks': 0,
            'conversions': 0,
            'revenue': 0.0
        }

    def run(self, duration_minutes=45, task_type='midday_check'):
        """
        Simulates performance analysis.
        In a real system, this would pull data from platform APIs, landing page analytics,
        and affiliate network reports.
        """
        print(f"[{time.strftime('%H:%M:%S')}] Analytics Agent: Starting task: {task_type}. Duration: {duration_minutes} minutes.")

        # Simulate fetching and analyzing data
        time.sleep(1)

        # Generate plausible but random data for the simulation
        views = random.randint(10000, 25000)
        clicks = int(views * random.uniform(0.01, 0.03)) # 1-3% CTR
        conversions = int(clicks * random.uniform(0.02, 0.05)) # 2-5% CVR
        revenue = conversions * random.uniform(15.0, 40.0) # Assume avg payout between $15-$40 for SaaS

        self.daily_performance['views'] += views
        self.daily_performance['clicks'] += clicks
        self.daily_performance['conversions'] += conversions
        self.daily_performance['revenue'] += revenue

        print(f"[{time.strftime('%H:%M:%S')}] Analytics Agent: Analysis complete. Generating report.")
        self._generate_report()

        return {"status": "complete", "report_generated": True, "data": self.daily_performance}

    def _generate_report(self):
        """Generates and prints a formatted performance dashboard."""

        # Calculate percentage changes (simulated)
        yesterday_revenue = self.daily_performance['revenue'] / (1 + random.uniform(-0.2, 0.2)) # Simulate yesterday's data
        revenue_change = ((self.daily_performance['revenue'] - yesterday_revenue) / yesterday_revenue) * 100 if yesterday_revenue else 100

        print("\n--- 📊 Daily Performance Dashboard 📊 ---")
        print(f"| Total Views:       | {self.daily_performance['views']:,}")
        print(f"| Total Clicks:      | {self.daily_performance['clicks']:,}")
        print(f"| Total Conversions: | {self.daily_performance['conversions']}")
        print(f"| Total Revenue:     | ${self.daily_performance['revenue']:.2f} ({revenue_change:+.1f}%)")
        print("------------------------------------------")

        # Simulate generating alerts and opportunities
        if random.random() < 0.3: # 30% chance of an alert
            print("| ⚠️  Alerts:")
            print("|   - Low conversion rate on 'Content Piece X'. Recommend review.")

        if random.random() < 0.5: # 50% chance of an opportunity
            print("| 🚀 Opportunities:")
            print("|   - 'Personal Journey' content style is performing well. Recommend creating more.")
        print("------------------------------------------\n")
