
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <link rel="icon" href="assets/images/logo-sacco.png" type="image/x-icon">
  <title>Sign Page | T-Bank</title>

  <!-- Bootstrap CSS CDN -->

<body style="background-color: rgba(46, 51, 52, 1)">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"
    integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4" crossorigin="anonymous">


  <!-- Font Awesome JS -->
  <script defer src="https://use.fontawesome.com/releases/v5.0.13/js/solid.js"
    integrity="sha384-tzzSw1/Vo+0N5UhStP3bvwWPq+uvzCMfrN1fEFe+xBmv1C/AtVX5K0uZtmcHitFZ"
    crossorigin="anonymous"></script>
  <script defer src="https://use.fontawesome.com/releases/v5.0.13/js/fontawesome.js"
    integrity="sha384-6OIrr52G08NpOFSZdxxz1xdNSndlD4vdcf/q2myIUVO0VsqaGHJsB0RaBE01VTOY"
    crossorigin="anonymous"></script>
  <link rel="stylesheet" type="text/css" href="/sacco/style/home.css">
  </head>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light" style="background-color: #008081">
      <div class="container-fluid">
        <p>


          <button style="z-index: 2" type="button" id="sidebarCollapse" class="btn btn-info">
            <i class="fa fa-home "></i>
            <span><a href="https://sacco.terrence-aluda.com/">Home Page</a></span>
          </button>
        <div class="d-flex justify-content-center" style="padding: 2%; text-align: center; background-color: #008081">
          <h1 style="color: white">T-BANK</h1>
        </div>
        </p>
      </div>
    </nav>
    <div class="d-flex align-items-center justify-content-center vw-60 vh-70" style="padding-bottom: 3vh">
      <div class="card border-dark  container">
        <div class="card-body border-dark row" style="background-color: #035050">
          <div id="sych" class=" col-md-6 d-flex align-items-center justify-content-center">
            <div class="card-body" style=" min-width: 30vw;">
              <div style="text-align: center; padding-bottom: 15vh" class="card-text text-white">
                <h3>Log in</h3>
              </div>
              <form action="https://sacco.terrence-aluda.com/sacco/backend/eng-ed-auth.php" method="post">
                  <div class="mb-3">
                    <div class="d-flex align-items-center justify-content-center vw-30">
                      <input class="form-control text-center" name="PhoneNo" type="text" autofocus="true" placeholder="Phone number"
                        id="signNum">
                    </div>
                  </div>
                  <div class="mb-3">
                    <div class="d-flex align-items-center justify-content-center vw-50">
                      <input type='password' name="password" class="form-control text-center" placeholder="Confirm password" id="logPass">
                    </div>
                  </div>
                  <div class="mb-3">
                    <div class="d-flex align-items-center justify-content-center vw-50">
                      <span id="banner" class="text-danger"></span>
                    </div>
                  </div>
                  <div class="mb-3" style="text-align: center">
                    <button id="logBtn" class="btn" style="background-color: red; color: white; "><i
                        class="fa fa-unlock-alt"></i> Log in</button>
                  </div>
             </form>
            </div>
          </div>
          <div style="background-image: url(assets/images/logo-big.jpeg); background-size: cover;" class="col-md-6">
            <div style="padding-top: 60vh"
              class="d-flex align-content-center align-items-center justify-content-center vw-100 vh-100">

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>

</html>