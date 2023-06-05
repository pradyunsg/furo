import { test, expect } from "@playwright/test";

test("footer snapshot has not changed", async ({ page }) => {
  await page.goto("");
  const footer = page.locator("footer");
  await expect(footer).toHaveScreenshot();
});
