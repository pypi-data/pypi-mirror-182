"use strict";

$(document).ready(function () {
    var data;
    var data_success = $(".successlist .successlist li");
    var data_info = $(".infolist .infolist li");
    var data_warning = $(".warninglist .warninglist li");
    var form_error = $(".errorlist .errorlist li");
    var data_danger = $(".customerrorlist .customerrorlist li");
    var alert_location = $(".alert-position li");
    alert_location = alert_location[0].textContent;
    var transition_in = $(".transition-in li");
    transition_in = transition_in[0].textContent;
    var transition_out = $(".transition-out li");
    transition_out = transition_out[0].textContent;
    var duration = $(".time li");
    duration = parseInt(duration[0].textContent);

    if (data_success.length > 0) {
        data = data_success;
    }
    else if (data_info.length > 0) {
        data = data_info;
    }
    else if (data_warning.length > 0) {
        data = data_warning;
    }
    else if (data_danger.length > 0) {
        data = data_danger;
    }
    else if (form_error.length > 0) {
        for (let i = 0; i < form_error.length; i++) {
            var txt = form_error[i].textContent;
            iziToast.error({
                title: "Error",
                message: txt,
                position: alert_location,
                transitionIn: transition_in,
                transitionOut: transition_out,
                timeout: duration,
                animateInside: true,
                balloon: false,
                pauseOnHover: true,
                progressBar: true,
                progressBarColor: '',
                progressBarEasing: 'linear',
            });
        }
    }

    if (data.length > 0) {
        for (let i = 0; i < data.length; i++) {
            let model = "";
            let message = "";

            if (i % 2 === 0) {
                model = data[i].textContent;
            }
            else{
                model = data[i - 1].textContent;
                message = data[i].textContent;
                if (model === "success") {
                    iziToast.success({
                        title: "Success",
                        message: message,
                        position: alert_location,
                        transitionIn: transition_in,
                        transitionOut: transition_out,
                        timeout: duration,
                        animateInside: true,
                        balloon: false,
                        pauseOnHover: true,
                        progressBar: true,
                        progressBarColor: '',
                        progressBarEasing: 'linear',
                    });
                }
                else if (model === "info") {
                    iziToast.info({
                        title: "Info",
                        message: message,
                        position: alert_location,
                        transitionIn: transition_in,
                        transitionOut: transition_out,
                        timeout: duration,
                        animateInside: true,
                        balloon: false,
                        pauseOnHover: true,
                        progressBar: true,
                        progressBarColor: '',
                        progressBarEasing: 'linear',
                    });
                }
                else if (model === "warning") {
                    iziToast.warning({
                        title: "Warning",
                        message: message,
                        position: alert_location,
                        transitionIn: transition_in,
                        transitionOut: transition_out,
                        timeout: duration,
                        animateInside: true,
                        balloon: false,
                        pauseOnHover: true,
                        progressBar: true,
                        progressBarColor: '',
                        progressBarEasing: 'linear',
                    });
                }
                else if (model === "danger") {
                    iziToast.error({
                        title: "Error",
                        message: message,
                        position: alert_location,
                        transitionIn: transition_in,
                        transitionOut: transition_out,
                        timeout: duration,
                        animateInside: true,
                        balloon: false,
                        pauseOnHover: true,
                        progressBar: true,
                        progressBarColor: '',
                        progressBarEasing: 'linear',
                    });
                }
            }
        }
    }
});
