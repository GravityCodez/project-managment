# ClassMic editable schedule

ClassMic_MS_Project_Schedule.xml contains seven work activities and four review or submission milestones, with finish-to-start dependencies. It includes 100 student hours, the selected dates and the published D/E/F deadline times. ClassMic_Schedule.csv supplies the same seven main activities in a simple table.

The seven-day scheduling calendar preserves the calendar-day windows in D3. Each scheduled day represents an eight-hour planning window; the separate Work field contains the estimated student effort. It does not assign either student eight hours of work every day.

Open the XML as a new project in Microsoft Project, choose Gantt Chart view, and show Name, Duration, Start, Finish, Predecessors and Work. Check the two seven-day sprint windows before exporting a chart. The file was generated in Microsoft's exchange format and checked for dates, dependencies and effort arithmetic. Microsoft Project is not available through the connected apps, so a native import or chart export has not been verified here.

The D3 brief asks for a chart from MS Project. The Word plan includes a readable Gantt view, and this XML supplies the editable source for a native chart. That chart-export requirement remains open until the file is opened there or the instructor accepts the supplied representation.

Format references: [Microsoft Project XML data introduction](https://learn.microsoft.com/en-us/office-project/xml-data-interchange/introduction-to-project-xml-data?view=project-client-2016), [task elements](https://github.com/MicrosoftDocs/office-developer-msproject-xml-docs/blob/main/project-xml-data-interchange/task-elements-and-xml-structure.md), and [dependency types](https://github.com/MicrosoftDocs/office-developer-msproject-xml-docs/blob/main/project-xml-data-interchange/type-element-multiple-parents.md).
