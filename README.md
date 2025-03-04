# Blue Sky Robotics - Robotica Animation Pipeline Tools
Capabilities: robotic motion data import/export (via CSV)
Coming soon: IK/FK switching on robotic rig

<img width="608" alt="selection" src="https://github.com/user-attachments/assets/1c51a8fc-f7f0-4e94-a637-55394db7a754" />

<h1>How to Export CSV Data</h1>
<ul>
  <li>Select all six joint controllers (recommend saving selection using selection sets add-on: https://captainhansode.gumroad.com/l/wqaMJ?layout=profile&recommended_by=library</li>
  <li>Under "Output Properties", set the export location under the output filepath dialog box (see figure below)</li>
  <li>Open "export-csv.py" in Scripting tab</li>
  <li>Click "Run Script" button</li>
  <li>Exported CSV file ("rotation-data-YYMMDD") can be found at set export location</li>
  <br>
  <img width="1217" alt="export-filepath" src="https://github.com/user-attachments/assets/c0746a98-f8eb-46da-83b0-be7b900df142" />
</ul>

<h1>How to Import CSV Data</h1>
<ul>
  <li>Open "import-csv.py" in Scripting tab</li>
  <li>On line 32, replace the current file path with the full file path of CSV file to import (see figure below)</li>
  <li>Click "Run Script" button</li>
</ul>
<img width="968" alt="import-filepath" src="https://github.com/user-attachments/assets/dab5ab61-4cea-42de-988a-86643b987bb3" />
