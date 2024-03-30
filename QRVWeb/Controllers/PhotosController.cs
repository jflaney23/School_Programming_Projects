using Microsoft.AspNetCore.Mvc;
using System.Text.Encodings.Web;

namespace QRVWeb.Controllers;

public class PhotosController : Controller
{
    public IActionResult Index()
    {
        return View();
    }
}