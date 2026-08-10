import puppeteer from "puppeteer-core";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { execSync } from "node:child_process";

const root = path.dirname(fileURLToPath(import.meta.url));
const url = process.argv[2] || "http://localhost:3000";
const label = process.argv[3] || "";
const fullPage = !process.argv.includes("--viewport-only");

function findChrome() {
  const cacheDir = path.join(process.env.HOME, ".cache/puppeteer/chrome");
  const versions = fs.readdirSync(cacheDir).sort().reverse();
  for (const v of versions) {
    const p = path.join(cacheDir, v, "chrome-mac-arm64", "Google Chrome for Testing.app", "Contents", "MacOS", "Google Chrome for Testing");
    if (fs.existsSync(p)) return p;
  }
  throw new Error("No cached Chrome for Testing found");
}

const outDir = path.join(root, "temporary screenshots");
fs.mkdirSync(outDir, { recursive: true });
let n = 1;
while (fs.existsSync(path.join(outDir, `screenshot-${n}${label ? "-" + label : ""}.png`))) n++;
const outFile = path.join(outDir, `screenshot-${n}${label ? "-" + label : ""}.png`);

const browser = await puppeteer.launch({
  executablePath: findChrome(),
  headless: true,
  args: ["--no-sandbox"],
});
const page = await browser.newPage();
await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 });
await page.goto(url, { waitUntil: "networkidle0", timeout: 30000 });

// walk the page so scroll-triggered reveal animations fire before capture
const scrollHeight = await page.evaluate(() => document.body.scrollHeight);
for (let y = 0; y < scrollHeight; y += 500) {
  await page.evaluate((y) => window.scrollTo(0, y), y);
  await new Promise(r => setTimeout(r, 60));
}
await page.evaluate(() => window.scrollTo(0, 0));
await new Promise(r => setTimeout(r, 500));

await page.screenshot({ path: outFile, fullPage });
await browser.close();
console.log(outFile);
