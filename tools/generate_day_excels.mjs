import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const root = path.resolve(import.meta.dirname, "..");
const wordDir = path.join(root, "content", "wordlists", "cet4_combined");
const outputDir = path.join(wordDir, "excel");
const previewDir = path.join(root, "_site", "excel-previews");
await fs.mkdir(outputDir, { recursive: true });
await fs.mkdir(previewDir, { recursive: true });

for (let day = 1; day <= 95; day += 1) {
  const filename = `day-${String(day).padStart(3, "0")}.json`;
  const data = JSON.parse(await fs.readFile(path.join(wordDir, filename), "utf8"));
  const workbook = Workbook.create();
  const sheet = workbook.worksheets.add(`Day ${day}`);
  sheet.showGridLines = false;
  sheet.freezePanes.freezeRows(3);

  sheet.getRange("A1:E1").merge();
  sheet.getRange("A1").values = [[`Day ${day} 四级词汇`]];
  sheet.getRange("A2:E2").merge();
  sheet.getRange("A2").values = [[`共 ${data.items.length} 个单词，来源：四级目录综合词汇`]];
  sheet.getRange("A3:E3").values = [["序号", "英文单词", "中文释义", "音标", "其他释义"]];
  sheet.getRange(`A4:E${data.items.length + 3}`).values = data.items.map((item, index) => [
    index + 1,
    item.word,
    item.meaning,
    item.phonetic || "",
    (item.alternatives || []).join("；"),
  ]);

  const used = sheet.getRange(`A1:E${data.items.length + 3}`);
  used.format.font = { name: "Arial", size: 10, color: "#1C2922" };
  used.format.verticalAlignment = "center";
  sheet.getRange("A1:E1").format = {
    font: { name: "Arial", size: 15, bold: true, color: "#1C2922" },
    rowHeight: 30,
  };
  sheet.getRange("A2:E2").format = {
    font: { name: "Arial", size: 10, italic: true, color: "#68756D" },
    rowHeight: 22,
  };
  sheet.getRange("A3:E3").format = {
    fill: "#3B9469",
    font: { name: "Arial", size: 10, bold: true, color: "#FFFFFF" },
    horizontalAlignment: "center",
    verticalAlignment: "center",
    rowHeight: 24,
    borders: { preset: "inside", style: "thin", color: "#FFFFFF" },
  };
  sheet.getRange(`A4:A${data.items.length + 3}`).format.horizontalAlignment = "center";
  sheet.getRange(`A4:E${data.items.length + 3}`).format.borders = {
    bottom: { style: "thin", color: "#E3EAE4" },
  };
  sheet.getRange(`A4:E${data.items.length + 3}`).format.rowHeight = 22;
  sheet.getRange(`C4:C${data.items.length + 3}`).format.wrapText = true;
  sheet.getRange(`E4:E${data.items.length + 3}`).format.wrapText = true;
  sheet.getRange("A:A").format.columnWidth = 8;
  sheet.getRange("B:B").format.columnWidth = 22;
  sheet.getRange("C:C").format.columnWidth = 46;
  sheet.getRange("D:D").format.columnWidth = 22;
  sheet.getRange("E:E").format.columnWidth = 38;

  workbook.recalculate();
  const check = await workbook.inspect({
    kind: "table",
    sheetId: sheet.name,
    range: `A1:E${Math.min(data.items.length + 3, 8)}`,
    include: "values,formulas",
    tableMaxRows: 8,
    tableMaxCols: 5,
  });
  if (!check.ndjson.includes(data.items[0].word)) throw new Error(`Day ${day} verification failed`);
  const errors = await workbook.inspect({
    kind: "match",
    searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!",
    options: { useRegex: true, maxResults: 20 },
    summary: `Day ${day} formula error scan`,
  });
  if (/"address"/.test(errors.ndjson)) throw new Error(`Day ${day} contains formula errors`);

  const output = await SpreadsheetFile.exportXlsx(workbook);
  const outputPath = path.join(outputDir, `day ${day}.xlsx`);
  await output.save(outputPath);
  await fs.rm(`${outputPath}.inspect.ndjson`, { force: true });
  const preview = await workbook.render({ sheetName: sheet.name, range: "A1:E12", scale: 1 });
  await fs.writeFile(path.join(previewDir, `day-${String(day).padStart(3, "0")}.png`), new Uint8Array(await preview.arrayBuffer()));
  process.stdout.write(`Day ${day}: ${data.items.length} words\n`);
}

const indexPath = path.join(wordDir, "index.json");
const index = JSON.parse(await fs.readFile(indexPath, "utf8"));
for (const day of index.days) day.excel_file = `excel/day ${day.day}.xlsx`;
await fs.writeFile(indexPath, `${JSON.stringify(index, null, 2)}\n`, "utf8");

for (const day of [1, 50, 95]) {
  const outputPath = path.join(outputDir, `day ${day}.xlsx`);
  const imported = await SpreadsheetFile.importXlsx(await FileBlob.load(outputPath));
  const sheet = imported.worksheets.getItem(`Day ${day}`);
  const source = JSON.parse(await fs.readFile(path.join(wordDir, `day-${String(day).padStart(3, "0")}.json`), "utf8"));
  const check = await imported.inspect({ kind: "table", sheetId: sheet.name, range: "A1:E6", include: "values,formulas", tableMaxRows: 6, tableMaxCols: 5 });
  if (!check.ndjson.includes(source.items[0].word)) throw new Error(`Saved Day ${day} workbook verification failed`);
  await fs.rm(`${outputPath}.inspect.ndjson`, { force: true });
}
