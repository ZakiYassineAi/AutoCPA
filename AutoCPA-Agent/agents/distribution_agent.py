import json
import os
import time
import random

class DistributionAgent:
    def __init__(self, content_path='data/content_archive/batch_001.json'):
        print("Initializing Distribution Agent...")
        self.content_archive = self._load_content(content_path)
        self.safety_limits = self._get_safety_limits()
        self.daily_post_counts = {
            'tiktok': 0,
            'instagram': 0,
            'pinterest': 0,
            'reddit': 0,
        }

    def _load_content(self, content_path):
        """Loads the content batch from the specified JSON file."""
        full_path = os.path.join('AutoCPA-Agent', content_path)
        try:
            with open(full_path, 'r') as f:
                data = json.load(f)
                print(f"Content loaded successfully from {full_path}. {len(data['content_batch'])} pieces found.")
                return data['content_batch']
        except FileNotFoundError:
            print(f"ERROR: Content file not found at {full_path}")
            return []
        except json.JSONDecodeError:
            print(f"ERROR: Could not decode JSON from {full_path}")
            return []

    def _get_safety_limits(self):
        """In a real implementation, this would load from config/platform_limits.json."""
        return {
            'tiktok': {'daily_posts': 3},
            'instagram': {'daily_posts': 2},
            'pinterest': {'daily_posts': 8},
            'reddit': {'weekly_posts': 7, 'daily_posts': 1}, # Simplified for daily check
        }

    def _select_content_for_platform(self, platform):
        """Selects a suitable piece of content for a given platform."""
        platform_content = [p for p in self.content_archive if p['platform'].lower() == platform.lower()]
        if not platform_content:
            return None
        return random.choice(platform_content)

    def run(self, duration_minutes=30):
        """
        Simulates the process of distributing content to platforms based on a priority map.
        """
        print(f"[{time.strftime('%H:%M:%S')}] Distribution Agent: Starting task. Duration: {duration_minutes} minutes.")

        # Priority defined in the prompt
        platform_priority = ['tiktok', 'instagram', 'youtube_shorts', 'pinterest', 'reddit']

        for platform in platform_priority:
            if self.daily_post_counts.get(platform, 0) < self.safety_limits.get(platform, {}).get('daily_posts', 1):
                content_piece = self._select_content_for_platform(platform)
                if content_piece:
                    print(f"-> Distributing to {platform.upper()}:")
                    print(f"   Content Type: {content_piece.get('content_type')}")
                    print(f"   Target Problem: {content_piece.get('target_problem')}")

                    # Simulate posting
                    time.sleep(0.5)

                    self.daily_post_counts[platform] = self.daily_post_counts.get(platform, 0) + 1
                    print(f"   SUCCESS. {platform.upper()} post count for today: {self.daily_post_counts[platform]}")
                else:
                    print(f"-> No suitable content found for {platform.upper()} in the archive.")
            else:
                print(f"-> Safety limit reached for {platform.upper()}. Skipping.")

        print(f"[{time.strftime('%H:%M:%S')}] Distribution Agent: Task complete.")
        return {"status": "complete", "platforms_updated": self.daily_post_counts}
