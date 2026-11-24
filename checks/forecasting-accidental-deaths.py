"""Recompute the Chapter 11 accidental-death forecast and its seasonal shape.

The January 1979 count is the first of the six months named in the
USAccDeaths documentation. It is not an entry of the fitted series, and the
sum of the twelve point forecasts is not an observed annual total.
"""
from pathlib import Path
import os
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "sources" / "book" / "chapters" / "11-forecasting.qmd"

r_home = os.environ.get("STATWIKI_R_HOME")
if r_home:
    R = str(Path(r_home) / "bin" / "exec" / "R")
else:
    R = shutil.which("R")
if not R or not os.access(R, os.X_OK):
    raise RuntimeError(
        "checks/forecasting-accidental-deaths.py requires R; install R or set STATWIKI_R_HOME."
    )

code = r"""
suppressPackageStartupMessages(library(forecast))
if (!requireNamespace("forecast", quietly=TRUE)) stop("forecast package is required")
x <- USAccDeaths
rd <- utils:::.getHelpFile(help("USAccDeaths"))
tmp <- tempfile()
tools::Rd2txt(rd, out=tmp, options=list(underline_titles=FALSE))
help <- paste(readLines(tmp, warn=FALSE), collapse="\n")
help <- gsub("_\010", "", help)
help <- gsub("\010", "", help)
flat <- gsub("[[:space:]]+", " ", help)
six <- sub(".*first six months of 1979 are ([0-9 ]+)\\..*", "\\1", flat)
fit <- auto.arima(x, seasonal=TRUE)
tr <- capture.output(auto.arima(x, seasonal=TRUE, trace=TRUE))
fc <- forecast(fit, h=12)
long <- as.numeric(forecast(fit, h=48)$mean)
h <- 14:48
op <- long[h] - long[h-1] - long[h-12] + long[h-13]
d1 <- diff(long)
rep <- max(abs(d1[13:(length(d1)-12)] - d1[25:length(d1)]))
inc <- long[13:24] - long[1:12]
inc2 <- long[25:36] - long[13:24]
ic <- deparse(formals(auto.arima)$ic)
cat("VERSION", as.character(packageVersion("forecast")), "\n")
cat("FREQ", frequency(x), "\n")
cat("START", start(x)[1], start(x)[2], "\n")
cat("END", end(x)[1], end(x)[2], "\n")
cat("N", length(x), "\n")
cat("MONTHLY", as.integer(grepl("monthly totals", flat)), "\n")
cat("SIX", six, "\n")
cat("INSERIES", as.integer(7798 %in% as.numeric(x)), "\n")
cat("ORDER", fit$arma[1], fit$arma[6], fit$arma[2], fit$arma[3], fit$arma[7], fit$arma[4], fit$arma[5], "\n")
cat("NAMES", paste(names(coef(fit)), collapse=","), "\n")
cat("COEF", paste(coef(fit), collapse=" "), "\n")
cat("JAN", as.numeric(fc$mean[1]), "\n")
cat("SUM", sum(fc$mean), "\n")
cat("LO80", fc$lower[1, "80%"], "\n")
cat("HI80", fc$upper[1, "80%"], "\n")
cat("LO95", fc$lower[1, "95%"], "\n")
cat("HI95", fc$upper[1, "95%"], "\n")
cat("IC", ic, "\n")
cat("DRIFT_TRACE", as.integer(any(grepl("with drift", tr))), "\n")
cat("OP", max(abs(op)), "\n")
cat("REPEAT", rep, "\n")
cat("INC0", inc[1], "\n")
cat("INCSPAN", max(abs(c(inc, inc2) - inc[1])), "\n")
"""
run = subprocess.run(
    [R, "--vanilla", "--slave"],
    input=code,
    text=True,
    capture_output=True,
)
if run.returncode != 0:
    detail = (run.stderr or run.stdout or "").strip()
    if "there is no package called" in detail and "forecast" in detail:
        raise RuntimeError(
            "checks/forecasting-accidental-deaths.py requires the forecast package; "
            "install.packages('forecast') and rerun. R itself is installed. " + detail
        )
    raise RuntimeError(detail or "R forecast check failed")
vals = {}
for line in run.stdout.splitlines():
    key, _, rest = line.partition(" ")
    vals[key] = rest.strip()

def fnum(key):
    return float(vals[key].split()[0])

assert vals["VERSION"]
assert int(vals["FREQ"]) == 12
assert vals["START"].split() == ["1973", "1"]
assert vals["END"].split() == ["1978", "12"]
assert int(vals["N"]) == 72
assert vals["MONTHLY"] == "1"
six = [int(v) for v in vals["SIX"].split()]
assert six == [7798, 7406, 8363, 8460, 9217, 9316]
assert sum(six) == 50560
assert vals["INSERIES"] == "0"
# arma vector is p, q, P, Q, period, d, D. The check prints p,d,q,P,D,Q,period.
assert vals["ORDER"].split() == ["0", "1", "1", "0", "1", "1", "12"]
assert vals["NAMES"] == "ma1,sma1"
coef = [float(v) for v in vals["COEF"].split()]
assert len(coef) == 2 and coef[0] < 0 and coef[1] < 0
assert abs(coef[0] + 0.4302692) < 1e-4
assert abs(coef[1] + 0.5527913) < 1e-4
jan = fnum("JAN")
total = fnum("SUM")
assert abs(jan - 8336.061) < 0.02 and round(jan) == 8336
assert abs(total - 109952.8) < 0.2 and round(total) == 109953
assert round(total) != sum(six)
assert fnum("LO95") < 7798 < fnum("HI95")
assert 7798 < jan
assert 7798 < fnum("LO80") < jan < fnum("HI80")
assert vals["IC"].replace(" ", "").startswith('c("aicc","aic","bic")')
assert vals["DRIFT_TRACE"] == "0"
assert fnum("OP") < 1e-6
assert fnum("REPEAT") < 1e-6
assert abs(fnum("INC0") - 186.523) < 0.01
assert fnum("INCSPAN") < 1e-6

def poly(t):
    return t * t

def twice(y, t):
    return y(t) - y(t - 1) - y(t - 12) + y(t - 13)

for t in (20, 40, 100):
    assert twice(poly, t) == 24
    assert twice(lambda s: 3 * s + 5, t) == 0
    assert twice(lambda s: (s % 12) + s, t) == 0

text = CHAPTER.read_text(encoding="utf-8")
assert "\r\n" not in text
deaths, _, rest = text.partition("## A hundred minutes of traffic")
assert "WWWusage" in rest and "auto.arima(WWWusage, seasonal = TRUE)" in rest
required = [
    "frequency $12$",
    "ARIMA$(0,1,1)(0,1,1)_{12}$",
    "with no constant",
    "AICc",
    '"aicc"',
    "$8336$",
    "$7798$",
    "$109{,}953$",
    "not an observed annual total",
    "first differences repeat every twelve months",
    "straight line plus a seasonal pattern",
    "does not follow a quadratic",
    "no drift",
    "auto.arima(USAccDeaths, seasonal = TRUE)",
    "{#fig-deaths-fc}",
    "{#fig-deaths-corr}",
    "{#fig-deaths}",
]
for token in required:
    assert token in deaths, token
assert "What supplies the seasonal period" in text
assert "(Usage, argument ic)" in deaths
rejected = [
    "was not told",
    "It found $12$",
    "about $8400$",
    "about $109{,}000$",
    "105{,}000$",
    "on top of the quadratic",
    "The AIC is what the function used",
    "read as behaviour",
]
for token in rejected:
    assert token not in text, token
# The diagnostic paragraph and exercise 1 still discuss a quadratic trend in the data.
assert deaths.count("quadratic trend") == 1
assert "A quadratic trend, differenced at lag $12$" in text
print(
    "forecasting-accidental-deaths: January forecast",
    round(jan),
    "observed January",
    six[0],
    "twelve-month forecast sum",
    round(total),
    "six documented 1979 months",
    sum(six),
    "forecast",
    vals["VERSION"],
)
