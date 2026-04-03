/** @odoo-module **/

import { Component, useState, onMounted } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class StudentDashboard extends Component {
    static template = "student_dashboard";

    setup() {
        this.orm = useService("orm");

        this.state = useState({
            totalStudent: 0,
            totalEnrollment: 0,
            totalCourse: 0,
            draft: 0,
            ongoing: 0,
            done: 0,
        });

        onMounted(() => {
            this.loadData();
        });
    }

    async loadData() {
        // total student
        this.state.totalStudent = await this.orm.searchCount("student.student", []);

        // total enrollment
        this.state.totalEnrollment = await this.orm.searchCount("course.enrollment", []);

        this.state.totalCourse = await this.orm.searchCount("course.course", []);

        // count per status
        this.state.draft = await this.orm.searchCount("course.enrollment", [['status','=','draft']]);
        this.state.ongoing = await this.orm.searchCount("course.enrollment", [['status','=','ongoing']]);
        this.state.done = await this.orm.searchCount("course.enrollment", [['status','=','done']]);

        this.renderChart();
    }

    renderChart() {
        const ctx = document.getElementById("myChart");

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Draft', 'Ongoing', 'Done'],
                datasets: [{
                    label: 'Enrollments',
                    data: [
                        this.state.draft,
                        this.state.ongoing,
                        this.state.done
                    ]
                }]
            }
        });
    }
}

registry.category("actions").add("student_dashboard", StudentDashboard);